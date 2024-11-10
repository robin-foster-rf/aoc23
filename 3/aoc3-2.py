# -*- coding: utf-8 -*-
"""
AOC 3.2

Created on Mon Dec  4 15:15:34 2023

@author: rfoster1
"""
import sys
import re
from typing import NamedTuple
from functools import reduce
import operator

re_digits = '\d+' # any group of digits
re_symbols = '[^.\d]' # anything that is not a dot or digit

# regular expression with two match groups, one for numbers and one for symbols
re_tok = '(?P<Number>%s)|(?P<Symbol>%s)' % (re_digits, re_symbols)

class Number(NamedTuple):
    value: int
    row: int
    startcol: int
    endcol: int 
    
class Symbol(NamedTuple):
    value: str
    row: int
    col: int

if __name__=="__main__":
    symbols = []
    numbers = []
    for i, line in enumerate(sys.stdin.readlines()):
        for m in re.finditer(re_tok, line.strip()):
            kind = m.lastgroup
            if kind == 'Number':
                value = int(m.group())
                startcol, endcol = m.span()
                endcol -= 1
                numbers.append(Number(value, i, startcol, endcol))
            elif kind == 'Symbol':
                value = m.group()
                col = m.start()
                symbols.append(Symbol(value, i, col))
    
    S = 0
    for s in symbols:
        gears = []
        if s.value == '*':
            for n in numbers:
                if n.row in (s.row-1, s.row+1):
                    if s.col>=n.startcol-1 and s.col<=n.endcol+1:
                        gears.append(n.value)
                elif n.row == s.row:
                    if s.col==n.endcol+1 or s.col==n.startcol-1:
                        gears.append(n.value)
        if len(gears)>1:
            S += reduce(operator.mul, gears, 1)
    
    print('Sum of gear ratios is', S)