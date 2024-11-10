# -*- coding: utf-8 -*-
"""
AOC1
https://adventofcode.com/2023/day/1

$ python aoc1.py < input.txt

Created on Fri Dec  1 11:25:04 2023

@author: rfoster1
"""
import sys

digits = '0123456789'

if __name__=="__main__":
    S = 0
    for line in sys.stdin.readlines():
        for c in line:
            if c in digits:
                d1 = int(c)
                break
        for c in reversed(line):
            if c in digits:
                d2 = int(c)
                break
        S += d1*10 + d2
    print("Sum is", S)