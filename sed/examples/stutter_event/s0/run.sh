#!/bin/bash

stage=0 # start from 0 if you need to start from data preparation
stop_stage=0

num_utts_per_shard=500

# Entire repo local dir, which should contain ./asr, ./data and ./sed
project_dir=/home/work_nfs4_ssd/hfxue/workspace/StutteringSpeechChallenge

# Please update the variable to include downloaded data:
raw_data_dir=/home/41_data/hfxue/corpus/Stutteringspeech

nj=16

train_set=train
dev_set=dev

train_config=conf/train_conformer.yaml
cmvn=true
dir=exp/conformer
checkpoint=

if [ ${stage} -le 0 ] && [ ${stop_stage} -ge 0 ]; then
  # Data preparation
  local/prepare_data.sh ${raw_data_dir} ${project_dir}/data || exit 1;
fi