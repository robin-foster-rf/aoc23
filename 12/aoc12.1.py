import sys
from functools import lru_cache

OPE = '.'
DAM = '#'
UNK = '?'

def parse_input():
    pats = []
    sigs = []
    for line in sys.stdin.readlines():
        pat, sig = line.strip().split(' ')
        sig = tuple(int(i) for i in sig.split(','))
        sigs.append(sig)
        pat = [x for x in pat.split('.') if x !='']
        pats.append('.'.join(pat))
    return pats, sigs

@lru_cache(maxsize=None)
def count(pat, sig):
    c = 0
    if not sig:
        if DAM in pat:
            return 0
        return 1
    if len(pat)<sig[0]:
        return 0
    if not OPE in pat[:sig[0]]:
        if len(pat)==sig[0] or pat[sig[0]]!=DAM:
            c += count(pat[sig[0]+1:],sig[1:])
    if pat[0] != DAM:
        c += count(pat[1:], sig)
    return c

if __name__=="__main__":
    pats, sigs = parse_input()
    S = 0
    for p, s in zip(pats, sigs):
        S += count(p,s)
    print(S)

    print(p, s)
