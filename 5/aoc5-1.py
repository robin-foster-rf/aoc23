# -*- coding: utf-8 -*-
"""
AOC 5.1 

Created on Tue Dec  5 16:59:23 2023

@author: rfoster1
"""
import sys
import re

re_tok = '(?P<Seeds>seeds: [\d ]+)|(?P<Maps>[a-z-]+ map:\n[\d+ \d+ \d+\n]+)'

if __name__=="__main__":
    # parse input
    ins = sys.stdin.read()
    maps = []
    for m in re.finditer(re_tok, ins):
        kind = m.lastgroup
        s = m.group()
        if kind=='Seeds':
            seeds = [int(i) for i in s.replace('seeds: ', '').split(' ')]
        elif kind=='Maps':
            map_name, rest = s.split(' map:\n')
            m = [[int(i) for i in row.split(' ') if i!=''] for row in rest.split('\n') if row!='']
            maps.append((map_name, m))
    
    seed_finals = []
    for s in seeds:
        for map_name, m in maps:
            for dest, source, step in m:
                if s>=source and s<(source+step):
                    s = dest + (s - source)
                    break
        seed_finals.append(s)

    print('Lowest location number is', min(seed_finals))    