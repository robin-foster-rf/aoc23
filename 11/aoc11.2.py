import sys
import re

from typing import Tuple

class Vec(object):
    def __init__(self, v: Tuple[int, ...]):
        self.v = v
    def __add__(self, other):
        return Vec(tuple(x+y for x, y in zip(self.v, other.v)))
    def __sub__(self, other):
        return Vec(tuple(x-y for x, y in zip(self.v, other.v)))
    def __str__(self):
        return str(self.v)
    def __repr__(self):
        return 'Vec({:})'.format(self)

def dist(a: Vec, b: Vec):
    c = a - b
    return sum(abs(i) for i in c.v)

def parse_input():
    galaxies = []
    empty_rows = []
    for row, line in enumerate(sys.stdin.readlines()):
        cols = list(m.start() for m in re.finditer('#', line))
        if not cols:
            empty_rows.append(row)
        galaxies += [(row, col) for col in cols]
    width = len(line.strip())
    occupied_cols = set(j for _, j in galaxies)
    empty_cols = list(j for j in range(width) if j not in occupied_cols)

    expanded_galaxies = []
    for i, j in galaxies:
        newj = j
        for col in empty_cols:
            if j>col: newj += int(1e6) - 1
        newi = i
        for row in empty_rows:
            if i>row: newi += int(1e6) - 1
        expanded_galaxies.append((newi, newj))
    return expanded_galaxies


if __name__=="__main__":
    galaxies = [Vec(g) for g in parse_input()]
    
    S = 0
    while galaxies:
        g1 = galaxies.pop()
        for g2 in galaxies:
            S += dist(g1, g2)
    print(S)