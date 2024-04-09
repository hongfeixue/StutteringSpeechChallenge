# -*- coding: utf-8 -*-

#!git clone https://github.com/wenet-e2e/wenet.git
#!cd wenet && pip3 install -r requirements.txt

import os, sys
import re
import wave
#import torchaudio
#import matplotlib.pyplot as plt

def remove_punc(txt):
  punc = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
  return re.sub(r"[%s]+" %punc, "",txt)

def sort_clean_txt(wavscp, text):
  os.rename(text, text+'.org')
  ids = []
  txt_dict = {}
  with open(wavscp) as scp, open(text+'.org') as f, open(text, 'w') as fo:
    for l in scp:
      l = l.strip()
      if not l: continue
      ids.append(l.split()[0])
    for l in f:
      l = l.strip()
      if not l: continue
      id_, *t = l.split()
      txt_dict[id_] = ' '.join(t)
    for id_ in ids:
      fo.write(f'{id_} {remove_punc(txt_dict[id_])}\n')

def collect_audio_len(wavscp):
  frames = {}
  paths = {}
  with open(wavscp) as f:
    for line in f.readlines():
      name, wav = line.strip().split()
      #meta = torchaudio.info(wav)
      #frames[name] = meta.num_frames

      # Open the audio file
      with wave.open(wav, 'rb') as fw:
        # Get the number of frames (samples)
        frames[name] = fw.getnframes()

      paths[name] = wav
  return frames, paths

def collect_text_len(text):
  num_char = {}
  texts = {}
  with open(text) as f:
    for line in f.readlines():
      try:
        name, t = line.strip().split(' ', 1)
        num_char[name] = len(t)
        texts[name] = t
      except:
        print(line)
  return num_char, texts

if __name__ == '__main__':
  data_dir, log = sys.argv[1:]

  for split in ['train', 'dev']:
    split_dir = os.path.join(data_dir, split)
    sort_clean_txt(os.path.join(split_dir, 'wav.scp'),
                  os.path.join(split_dir, 'text'))

  train_dir = os.path.join(data_dir, 'train')
  frames, paths = collect_audio_len(os.path.join(train_dir, 'wav.scp'))
  chars, texts = collect_text_len(os.path.join(train_dir, 'text'))

  #fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
  #axs[0].hist(frames.values(), bins=100)
  #axs[1].hist(chars.values(), bins=100)

  # filter out long audio and text
  # frame upper: 230000
  # char upper: 60
  os.rename(os.path.join(train_dir, 'wav.scp'), os.path.join(train_dir, 'wav.scp.old'))
  os.rename(os.path.join(train_dir, 'text'), os.path.join(train_dir, 'text.old'))
  with open(os.path.join(train_dir, 'wav.scp'), 'w') as fw, open(os.path.join(train_dir, 'text'), 'w') as ft, open(log, 'w') as flog:
    for name in chars:
      if frames[name] < 230000 and chars[name] < 60:
        fw.write(f'{name} {paths[name]}\n')
        ft.write(f'{name} {texts[name]}\n')
      else:
        flog.write(f'{name} {frames[name]} {chars[name]}\n')
