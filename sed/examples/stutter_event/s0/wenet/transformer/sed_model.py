# Copyright (c) 2020 Mobvoi Inc. (authors: Binbin Zhang, Di Wu)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Modified from ESPnet(https://github.com/espnet/espnet)

from typing import Dict, List, Optional, Tuple

import torch

from wenet.transformer.encoder import TransformerEncoder

class SEDModel(torch.nn.Module):
    """CTC-attention hybrid Encoder-Decoder model"""

    def __init__(
        self,
        vocab_size: int,
        encoder: TransformerEncoder,
    ):

        super().__init__()
        # note that eos is the same as sos (equivalent ID)
        self.sos = vocab_size - 1
        self.eos = vocab_size - 1
        self.vocab_size = vocab_size

        self.encoder = encoder
        self.linear = torch.nn.Linear(encoder.output_size(), vocab_size)
        self.loss_fn = torch.nn.MultiLabelSoftMarginLoss()

    @torch.jit.ignore(drop=True)
    def forward(
        self,
        speech: torch.Tensor,
        speech_lengths: torch.Tensor,
        text: torch.Tensor,
        text_lengths: torch.Tensor,
    ) -> Dict[str, Optional[torch.Tensor]]:
        """Frontend + Encoder + Calc loss

        Args:
            speech: (Batch, Length, ...)
            speech_lengths: (Batch, )
            text: (Batch, Length)
            text_lengths: (Batch,)
        """

        assert text_lengths.dim() == 1, text_lengths.shape
        # Check that batch_size is unified
        assert (speech.shape[0] == speech_lengths.shape[0] == text.shape[0] ==
                text_lengths.shape[0]), (speech.shape, speech_lengths.shape,
                                         text.shape, text_lengths.shape)
        # 1. Encoder
        encoder_output = self.encoder(speech, speech_lengths)
        if len(encoder_output) == 2:
            encoder_out, encoder_mask = encoder_output
            encoder_mask = encoder_mask.squeeze(1).unsqueeze(-1)
            encoder_out = encoder_out * encoder_mask
        else:
            encoder_out, _, _ = encoder_output
        encoder_out = encoder_out.mean(dim=1)
        encoder_out = self.linear(encoder_out)
        loss = self.loss_fn(encoder_out, text)

        return {"loss": loss}

    def _forward_encoder(
        self,
        speech: torch.Tensor,
        speech_lengths: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # Let's assume B = batch_size
        encoder_output = self.encoder(speech, speech_lengths)
        if len(encoder_output) == 2:
            encoder_out, encoder_mask = encoder_output
            encoder_mask = encoder_mask.squeeze(1).unsqueeze(-1)
            encoder_out = encoder_out * encoder_mask
        else:
            encoder_out, _, _ = encoder_output
        encoder_out = encoder_out.mean(dim=1)
        return encoder_out

    def decode(
        self,
        speech: torch.Tensor,
        speech_lengths: torch.Tensor
    ):
        """ Decode input speech

        Args:
            methods:(List[str]): list of decoding methods to use, which could
                could contain the following decoding methods, please refer paper:
                https://arxiv.org/pdf/2102.01547.pdf
                   * ctc_greedy_search
                   * ctc_prefix_beam_search
                   * atttention
                   * attention_rescoring
            speech (torch.Tensor): (batch, max_len, feat_dim)
            speech_length (torch.Tensor): (batch, )

        Returns: 
        """
        assert speech.shape[0] == speech_lengths.shape[0]
        encoder_out = self._forward_encoder(
            speech, speech_lengths)
        encoder_out = self.linear(encoder_out)
        results = torch.sigmoid(encoder_out)
        return results
