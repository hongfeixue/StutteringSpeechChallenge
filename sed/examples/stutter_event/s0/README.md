# Wenet
This code has addtional components for [Wenet](https://github.com/wenet-e2e/wenet) (git commit: 188e5e9c2c3250f4ed44af4a09d2a8866e4a0ab6). Please check `examples` and `wenet` folders.

SED is a multi-label multi-class tagging problem. By giving a stuttering speech audio snippet, the system aims to tag five stuttering events:

```
/p: prolongation
/b: block
/r: sound repetition
[]: word repetition
/i: interjection
```

## Data

We prepare the data by cutting long utterances into short snippets. The cut is done on the word time boundaries which have been identified by conducting forced alignment between the audios and the transcriptions.

The dataset contains 41953 audio snippets, of which the average length is 4.19s.

An annotation example:

```
Start,Stop,Category,Prolongation,Block,SoundRep,WordRep,Interjection,Text
104.09,105.68,A,0,0,0,0,0,我是。
106.3,108.94,A,0,0,0,1,0,零三[三]的，
108.94,119.12,A,0,0,1,1,0,口[口/r]吃患者。
119.13,124.49,A,0,0,0,0,0,我是从小就有口吃。
126.46,133.89,A,1,0,0,1,1,到[到]现在，嗯/i/p，一直。
136.61,141.33,A,0,0,0,0,1,伴随我，到我现在那嗯/i。
142.72,149.5,A,1,0,1,0,1,现在我已经工/r作了，嗯/i/p。
```

In Category, we have 3 kinds of labels. `A`: interviewee conversation (person who stutter), `B`: interviewer conversation (also person who stutter), `P`: interviewee command. 

## Results

Confomer + sigmoid cross entropy loss  
This is a model with 3 blocks Conformer encoder that is trained with sigmoid cross entropy loss.
Test:
```
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
```

Dev:
```
        /p      /b      /r      /wr     /i      avg
rec:    60.22   42.36   38.46   64.81   59.39   53.05
prec:   63.17   46.99   40.44   65.54   60.83   55.39
f1:     61.66   44.56   39.43   65.17   60.1    54.18
```
