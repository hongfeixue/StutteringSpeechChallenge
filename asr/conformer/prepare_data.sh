#!/bin/bash

stage=0
stop_stage=1

. src/tools/parse_options.sh || exit 1;

# Entire repo local dir, which should contain ./asr, ./data and ./sed
project_dir=/home/work_nfs4_ssd/hfxue/workspace/StutteringSpeechChallenge

# Please update the variable to include downloaded data:
raw_data_dir=/home/41_data/hfxue/corpus/Stutteringspeech

# Please update the variable to generate data
utts_data_dir=$project_dir/data/data_asr

data_dir=$project_dir/asr/conformer/data

if [ ${stage} -le 0 ] && [ ${stop_stage} -ge 0 ]; then
    # prepare utterance data
    for split in train dev; do
        python3 src/prepare_utts.py $raw_data_dir/$split $utts_data_dir/$split
    done
fi

if [ ${stage} -le 1 ] && [ ${stop_stage} -ge 1 ]; then
    # process wav.scp and text
    mkdir -p $data_dir

    for split in train dev; do
        rm -r $data_dir/$split
        mkdir -p $data_dir/$split
        ids=$(python3 src/get_ids.py $project_dir/data/level_split.json $split)
        echo $ids
        for i in ${ids}; do find $utts_data_dir/$split/${i} -name '*.wav' -exec sh -c 'for f do echo "$(echo ${f%.*}) $(echo $f)"; done' sh {} + >> $data_dir/$split/wav.scp; done
        for i in ${ids}; do find $utts_data_dir/$split/${i} -name '*.txt' -exec sh -c 'for f do echo "$(echo ${f%.*}) $(cat $f)"; done' sh {} + >> $data_dir/$split/text; done
    done

    # remove punctuation from text since Wenet model doesn't produce them
    # filter long utterances
    python3 src/clean_scp.py $data_dir $data_dir/filter.log
fi