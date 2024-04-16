#!/bin/python3
import sys, os

rootdir, test_sets = sys.argv[1:]

def calc_rec_prec_f1(hit, hyp, ref):
    rec = hit / ref
    prec = hit / hyp
    f1 = 2 * rec * prec / (rec + prec)
    return rec, prec, f1

def add_results(r, v):
    if r:
        r = list(map(lambda x, y: x + y, r, v))
    else:
        r = v
    return r

def print_results(r, l):
    rec = ['rec:']
    prec = ['prec:']
    f1 = ['f1:']
    for s in map(calc_rec_prec_f1, r['hit'], r['hyp'], r['ref']):
        rec.append("{:.2f}".format(s[0]*100))
        prec.append("{:.2f}".format(s[1]*100))
        f1.append("{:.2f}".format(s[2]*100))
    print('\t'+'\t'.join(l))
    print('\t'.join(rec))
    print('\t'.join(prec))
    print('\t'.join(f1))

results = {
    'hit': [],
    'hyp': [],
    'ref': []
}

results_conv = {
    'hit': [],
    'hyp': [],
    'ref': []
}

results_comm = {
    'hit': [],
    'hyp': [],
    'ref': []
}

for test_set in test_sets.split():
    stat_file = os.path.join(rootdir, test_set, 'results.txt')
    ctr = 0
    with open(stat_file, 'r') as file:
        for line in file:
            words = line.split()
            tag = words[0].strip(':')
            if tag in results:
                values = list(map(float, words[1:]))
                results[tag] = add_results(results[tag], values)
                if 'A' in test_set:
                    results_conv[tag] = add_results(results_conv[tag], values)
                if 'P' in test_set:
                    results_comm[tag] = add_results(results_comm[tag], values)
                ctr += 1
            if ctr >= 3:
                break

labels = ['/p', '/b', '/r', '[]', '/i']

print('all/all')
print_results(results, labels)
print('all/conv')
print_results(results_conv, labels)
print('all/comm')
print_results(results_comm, labels)