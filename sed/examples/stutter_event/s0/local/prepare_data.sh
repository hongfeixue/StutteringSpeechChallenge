#!/bin/bash

if [ $# != 2 ]; then
  echo "Usage: $0 <raw-audio-path> <audio-path>"
  exit 1;
fi

raw_data_dir=$1
data_dir=$2
train_dir=data/train
dev_dir=data/dev

mkdir -p $train_dir
mkdir -p $dev_dir

# data directory check
if [ ! -d $aishell_audio_dir ] || [ ! -f $aishell_text ]; then
  echo "Error: $0 requires two directory arguments"
  exit 1;
fi

for split in train dev; do
  rm data/$split/*
  ids=$(python3 local/get_ids.py $data_dir/level_split.json $split all)
  for i in ${ids}; do echo $raw_data_dir/$split/audio/${i}.wav >> data/$split/wav.flist; done
  for i in ${ids}; do echo $raw_data_dir/$split/Sed-ref/${i}.csv >> data/$split/ref.flist; done
done

# process train set
sed -e 's/\.csv//' $train_dir/ref.flist | awk -F '/' '{print $NF}' > $train_dir/utt.list
paste -d' ' $train_dir/utt.list $train_dir/wav.flist | sort -u > $train_dir/wav.scp
python3 local/process_segments.py $train_dir 0

sed -e 's/\.csv//' $dev_dir/ref.flist | awk -F '/' '{print $NF}' > $dev_dir/utt.list
paste -d' ' $dev_dir/utt.list $dev_dir/wav.flist | sort -u > $dev_dir/wav.scp
python3 local/process_segments.py $dev_dir 0

echo "$0: data preparation succeeded"
exit 0;
