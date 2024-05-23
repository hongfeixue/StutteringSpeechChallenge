# Wenet
This code is based on [Wenet](https://github.com/wenet-e2e/wenet) (git commit: 907e986ebd7f4de58c9ff54fc6e7b13bcb5c65da).

We trained a Conformer model using the AISHELL-1 and StutteringSpeech datasets and evaluated it on the test split of the StutteringSpeech dataset.

Please refer to `run.sh` for data preprocessing, training and evaluation. The traing config is located in `conf/train_u2++_conformer.yaml`.

## Results
The evaluation results of the Wenet Conformer model are as follows:

Test:
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

Dev:
```
all       |all         :        13.32 % N=53322 C=47972 D=1449 S=3901 I=1751
```
