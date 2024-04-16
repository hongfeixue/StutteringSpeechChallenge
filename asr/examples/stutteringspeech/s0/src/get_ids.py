import sys, os
import json

split_file, split = sys.argv[1:]

with open(os.path.join(split_file)) as f:
    splits = json.load(f)

ids = []
for level in splits:
    for id_ in splits[level][split]:
        ids.append(id_)

print(' '.join(ids))