# Task I
Please refer to `sed/stutter_event/run.sh` for SED data preprocessing.

Please refer to `sed/examples/stutter_event/s0/run.sh` for SED baseline system.

## SED Results
The evaluation results of the Conformer model are as follows:

all/all
        /p      /b      /r      []      /i      avg
rec:    59.79   15.09   35.03   62.70   79.80   50.48
prec:   60.46   33.73   54.91   58.52   67.83   55.09
f1:     60.12   20.86   42.77   60.54   73.33   51.52
all/conv
        /p      /b      /r      []      /i      avg
rec:    57.22   7.87    22.02   63.94   79.25   46.06
prec:   64.96   45.16   41.62   62.28   71.18   57.04
f1:     60.85   13.40   28.80   63.10   75.00   48.23
all/comm
        /p      /b      /r      []      /i      
rec:    65.43   21.76   49.84   59.70   83.82   56.11
prec:   53.36   31.11   65.42   50.59   51.24   50.34
f1:     58.78   25.61   56.58   54.77   63.60   51.87

# Task II
Please refer to `asr/conformer/prepare_data.sh` for ASR data preprocessing.

Please refer to `asr/examples/stutteringspeech/s0/run.sh` for ASR baseline system.

## ASR Results
The evaluation results of the Conformer model are as follows:

Level     |Category
----------|------------
mild      |conversation:        WER=16.17% N= 92786 C= 81594 D=2986 S=8206 I=3814
moderate  |conversation:        WER=17.80% N= 15122 C= 13291 D= 539 S=1292 I= 860
severe    |conversation:        WER=29.48% N= 12732 C= 10277 D= 695 S=1760 I=1299
mild      |command     :        WER=17.48% N= 43698 C= 36262 D=1105 S=6331 I= 201
moderate  |command     :        WER=20.14% N=  6747 C=  5448 D= 194 S=1105 I=  60
severe    |command     :        WER=27.54% N= 12273 C=  9045 D= 693 S=2535 I= 152
mild      |all         :        WER=16.59% N=136484 C=117856 D=4091 S=14537 I=4015
moderate  |all         :        WER=18.52% N= 21869 C= 18739 D= 733 S=2397 I= 920
severe    |all         :        WER=28.53% N= 25005 C= 19322 D=1388 S=4295 I=1451
all       |conversation:        WER=17.78% N=120640 C=105162 D=4220 S=11258 I=5973
all       |command     :        WER=19.73% N= 62718 C= 50755 D=1992 S=9971 I= 413
all       |all         :        WER=18.45% N=183358 C=155917 D=6212 S=21229 I=6386