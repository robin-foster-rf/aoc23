# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:44:45 2023

@author: rfoster1
"""
import sys

if __name__=="__main__":
    pts = []
    for line in sys.stdin.readlines():
        card, rest = line.split(':')
        card = int(card.split(' ')[-1])
        wins, mine = rest.split('|')
        wins = {int(i) for i in wins.strip().split(' ') if i!=''}
        mine = {int(i) for i in mine.strip().split(' ') if i!=''}

        pts.append(len(mine.intersection(wins)))
    copies = [1 for i in range(card)]
    for i, pt in enumerate(pts):
        for j in range(pt):
            copies[i+j+1] += copies[i]
    print('Total scratchcards', sum(copies))