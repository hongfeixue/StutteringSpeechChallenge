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
mild      |conversation:        CER=16.17% N= 92786 C= 81594 D=2986 S=8206 I=3814
moderate  |conversation:        CER=17.80% N= 15122 C= 13291 D= 539 S=1292 I= 860
severe    |conversation:        CER=29.48% N= 12732 C= 10277 D= 695 S=1760 I=1299
mild      |command     :        CER=17.48% N= 43698 C= 36262 D=1105 S=6331 I= 201
moderate  |command     :        CER=20.14% N=  6747 C=  5448 D= 194 S=1105 I=  60
severe    |command     :        CER=27.54% N= 12273 C=  9045 D= 693 S=2535 I= 152
mild      |all         :        CER=16.59% N=136484 C=117856 D=4091 S=14537 I=4015
moderate  |all         :        CER=18.52% N= 21869 C= 18739 D= 733 S=2397 I= 920
severe    |all         :        CER=28.53% N= 25005 C= 19322 D=1388 S=4295 I=1451
all       |conversation:        CER=17.78% N=120640 C=105162 D=4220 S=11258 I=5973
all       |command     :        CER=19.73% N= 62718 C= 50755 D=1992 S=9971 I= 413
all       |all         :        CER=18.45% N=183358 C=155917 D=6212 S=21229 I=6386
```

Dev:
```
all       |all         :        CER=14.85 % N=95612 C=85106 D=2770 S=7736 I=3692
```
