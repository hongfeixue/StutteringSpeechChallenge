# Task I
Please refer to `sed/stutter_event/run.sh` for SED data preprocessing.

Please refer to `sed/examples/stutter_event/s0/run.sh` for SED baseline system.

## SED Results
The evaluation results of the Conformer model are as follows:
```
        /p      /b      /r      []      /i      avg

Rec:    64.9    17.9    35.06   66.32   81.39   53.11
Prec:   65.33   37.83   51.92   57.93   69.32   56.47
F1:     65.12   24.3    41.86   61.85   74.87   53.60
```

# Task II
Please refer to `asr/conformer/prepare_data.sh` for ASR data preprocessing.

Please refer to `asr/examples/stutteringspeech/s0/run.sh` for ASR baseline system.

## ASR Results
The evaluation results of the Conformer model are as follows:
```
Level     |Category
----------|------------
mild      |conversation:        WER=15.94% N= 56205 C= 49345 D=1801 S=5059 I=2100
moderate  |conversation:        WER=17.50% N=  9115 C=  8028 D= 292 S= 795 I= 508
severe    |conversation:        WER=30.95% N=  7602 C=  6073 D= 460 S=1069 I= 824
mild      |command     :        WER=19.55% N= 32838 C= 26566 D=1701 S=4571 I= 149
moderate  |command     :        WER=22.72% N=  5413 C=  4212 D= 354 S= 847 I=  29
severe    |command     :        WER=28.25% N=  8480 C=  6156 D= 612 S=1712 I=  72
mild      |all         :        WER=17.27% N= 89043 C= 75911 D=3502 S=9630 I=2249
moderate  |all         :        WER=19.45% N= 14528 C= 12240 D= 646 S=1642 I= 537
severe    |all         :        WER=29.53% N= 16082 C= 12229 D=1072 S=2781 I= 896
all       |conversation:        WER=17.70% N= 72922 C= 63446 D=2553 S=6923 I=3432
all       |command     :        WER=21.50% N= 46731 C= 36934 D=2667 S=7130 I= 250
all       |all         :        WER=19.18% N=119653 C=100380 D=5220 S=14053 I=3682
```
