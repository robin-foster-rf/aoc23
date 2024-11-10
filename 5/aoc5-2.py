import sys
import re

SEEDS_RE = r'(?P<SEEDS>seeds: [\d+ ]+)'
MAP_RE = r'(?P<MAP>\w+-\w+-\w+ map:\n(?:(?:\d+ \d+ \d+)\n)+)'
TOK_RE = SEEDS_RE + '|' + MAP_RE

def parse_input(ins):
    maps = []
    for m in re.finditer(TOK_RE, ins):
        if m.lastgroup=='SEEDS':
            s = m.group()
            s = s.split(':')[-1]
            seeds = [int(n) for n in s.strip().split(' ') if n!='']
            seeds = list(zip(seeds[0::2], seeds[1::2]))
        elif m.lastgroup=='MAP':
            s = m.group()
            map_name, s = s.split(' map:\n')
            triples = [
                tuple(int(i) for i in T.split(' ')) 
                    for T in s.split('\n') if T!=''
            ]
            maps.append((map_name, triples))
    return seeds, maps

def inv_map(n, map):
    for d, s, sp in map:
        if (n>=d):
            if (n<d+sp):
                return n + s - d
    return n

def traceback(n, maps):
    for map in reversed(maps):
        n = inv_map(n, map)
    return n

def s_in_seeds(s, seeds):
    for start, span in seeds:
        if (s>=start):
            if (s<start+span):
                return True
    return False

if __name__=="__main__":
    seeds, maps = parse_input(sys.stdin.read())
    maps = [m[1] for m in maps]

    ns = [n[0] for n in maps[-1]]
    ns.sort()

    n = 0
    while True:
        s = traceback(n, maps)
        if s_in_seeds(s, seeds):
            print('Solution n = ', n)
            break
        n += 1
        if n%1000000==0:
            print(n)
