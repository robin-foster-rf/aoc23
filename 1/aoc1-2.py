# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:46:14 2023

@author: rfoster1
"""
import sys

digits = '0123456789'
words = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

if __name__=="__main__":
    S = 0
    for line in sys.stdin.readlines():
        d1, d2 = 0, 0
        for i1, c in enumerate(line):
            if c in digits:
                d1 = int(c)
                break
        for i2, c in enumerate(reversed(line)):
            if c in digits:
                d2 = int(c)
                i2 = len(line) - i2 - 1
                break
        
        for d, s in zip(range(1,10), words):
            i = line.find(s)
            if (i!=-1) and (i<i1):
                d1 = d
                i1 = i
            i = line.rfind(s)
            if (i!=-1) and (i>i2):
                d2 = d
                i2 = i
        
        S += d1*10 + d2
    print("Sum is", S)