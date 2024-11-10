# -*- coding: utf-8 -*-
"""
AOC 4.1

Created on Tue Dec  5 16:23:17 2023

@author: rfoster1
"""
import sys

if __name__=="__main__":
    S = 0
    for line in sys.stdin.readlines():
        card, rest = line.split(':')
        wins, mine = rest.split('|')
        wins = {int(i) for i in wins.strip().split(' ') if i!=''}
        mine = {int(i) for i in mine.strip().split(' ') if i!=''}
        pts = len(mine.intersection(wins))
        if pts>0:
            S += 2**(pts-1)
    print('Total points', S)