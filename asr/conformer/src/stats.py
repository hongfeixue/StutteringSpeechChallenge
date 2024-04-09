import sys, os
import json
import re
from collections import defaultdict

def calc_wer(wer, level, category):
    ref_all, cor_all, sub_all, del_all, ins_all = 0, 0, 0, 0, 0
    
    if level is None:
        wer_level = [s  for l in wer for s in wer[l]]
    else:
        wer_level = wer[level]
        
    for name, (ref, cor, sub, dele, ins) in wer_level:
        if category is None or category in name:
            ref_all += ref
            cor_all += cor
            sub_all += sub
            del_all += dele
            ins_all += ins
    err_all = sub_all + del_all + ins_all
    if level is None:
        level = 'all'
    if category is None:
        category = 'all'
    return f'{level:<10}|{category:<12}:\tWER={(err_all / ref_all) * 100:5.2f}% N={int(ref_all):6d} C={int(cor_all):6d} D={int(del_all):4d} S={int(sub_all):4d} I={int(ins_all):4d}\n'

def calc_wer_id(wer, level, id_, category):
    ref_all, cor_all, sub_all, del_all, ins_all = 0, 0, 0, 0, 0
    for name, (ref, cor, sub, dele, ins) in wer[level]:
        if (category is None or category in name) and id_ in name.split('_')[0]:
            ref_all += ref
            cor_all += cor
            sub_all += sub
            del_all += dele
            ins_all += ins
    err_all = sub_all + del_all + ins_all
    if category is None:
        category = 'all'
    return f'{id_:<10}|{category:<12}:\tWER={(err_all / ref_all) * 100:5.2f}% N={int(ref_all):4d} C={int(cor_all):4d} D={int(del_all):3d} S={int(sub_all):3d} I={int(ins_all):3d}\n'

if __name__ == '__main__':	
    exp_dir, split_file, stats_file = sys.argv[1:]

    with open(os.path.join(split_file)) as f:
        splits = json.load(f)

    ids = defaultdict(set)
    for level in splits:
        ids[level] = set(splits[level]['test'])

    # {'mild': [[name, wer]]}
    wer = defaultdict(list)
    last_level = ''

    WER=r'WER: .+ N=(.+) C=(.+) S=(.+) D=(.+) I=(.+)'

    with open(os.path.join(exp_dir, 'wer')) as f:
        for l in f:
            l = l.strip()
            if not l: continue
            if l.startswith('utt:'):
                _, name = l.split()
                subpath = name.split('/')
                id_ = subpath[-2]
                filename = subpath[-1]
                filename = id_ + '_' + filename
                if id_ in ids['mild']:
                    wer['mild'].append([filename, None])
                    last_level = 'mild'
                elif id_ in ids['moderate']:
                    wer['moderate'].append([filename, None])
                    last_level = 'moderate'
                elif id_ in ids['severe']:
                    wer['severe'].append([filename, None])
                    last_level = 'severe'
            if l.startswith('WER:'):
                assert wer[last_level][-1][1] is None
                
                m = re.match(WER, l)
                assert m is not None
                wer[last_level][-1][1] = (float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), float(m.group(5)))

    with open(stats_file, 'w') as f:
        f.write('Overall stats:\n')
        f.write(f'Level     |Category\n')
        f.write('----------|------------\n')
        f.write(calc_wer(wer, 'mild', 'conversation'))
        f.write(calc_wer(wer, 'moderate', 'conversation'))
        f.write(calc_wer(wer, 'severe', 'conversation'))

        f.write(calc_wer(wer, 'mild', 'command'))
        f.write(calc_wer(wer, 'moderate', 'command'))
        f.write(calc_wer(wer, 'severe', 'command'))

        f.write(calc_wer(wer, 'mild', None))
        f.write(calc_wer(wer, 'moderate', None))
        f.write(calc_wer(wer, 'severe', None))

        f.write(calc_wer(wer, None, 'conversation'))
        f.write(calc_wer(wer, None, 'command'))
        f.write(calc_wer(wer, None, None))

        f.write('\nPer-spk stats:\n')	
        for level in ids:
            f.write(level+'\n')	
            f.write('----------|------------\n')
            for id_ in ids[level]:
                f.write(calc_wer_id(wer, level, id_, 'conversation'))
                f.write(calc_wer_id(wer, level, id_, 'command'))
                f.write(calc_wer_id(wer, level, id_, None))