# -*- coding: utf-8 -*-
"""
AOC 3.1

Created on Mon Dec  4 15:15:34 2023

@author: rfoster1
"""
import sys
import re
from typing import NamedTuple

re_digits = '\d+' # any group of digits
re_symbols = '[^.\d]' # anything that is not a dot or digit

# regular expression with two match groups, one for numbers and one for symbols
re_tok = '(?P<Number>%s)|(?P<Symbol>%s)' % (re_digits, re_symbols)

class Number(NamedTuple):
    value: int
    row: int
    startcol: int
    endcol: int 

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
                col = m.start()
                symbols.append((i, col))
    
    symbol_boundaries = [
        (i, j) for I,J in symbols
        for i in (I-1, I, I+1) 
        for j in (J-1, J, J+1)
    ]
    
    S = 0
    for n in numbers:
        nlocs = [(n.row, c) for c in range(n.startcol, n.endcol+1)]
        for nloc in nlocs:
            if nloc in symbol_boundaries:
                S += n.value
                break
    print('Sum of part numbers is', S)