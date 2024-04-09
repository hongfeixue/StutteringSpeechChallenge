import sys, os, json

split_file, split, level = sys.argv[1:]

with open(os.path.join(split_file)) as f:
    splits = json.load(f)

ids = []
if level == 'all':
    for level in splits:
        for id_ in splits[level][split]:
            ids.append(id_)
else:
    for id_ in splits[level][split]:
        ids.append(id_)

print(' '.join(ids))