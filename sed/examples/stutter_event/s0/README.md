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
        /p      /b      /r      []      /i      avg

Rec:    64.9    17.9    35.06   66.32   81.39   53.11
Prec:   65.33   37.83   51.92   57.93   69.32   56.47
F1:     65.12   24.3    41.86   61.85   74.87   53.60
```

Dev:
```
        /p      /b      /r      /wr     /i      avg
Rec:    60.22   42.36   38.46   64.81   59.39   53.05
Prec:   63.17   46.99   40.44   65.54   60.83   55.39
F1:     61.66   44.56   39.43   65.17   60.1    54.18
```
