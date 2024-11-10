# -*- coding: utf-8 -*-
"""
AOC 2.2

Created on Mon Dec  4 15:06:08 2023

@author: rfoster1
"""
import sys

R, G, B = 12, 13, 14

if __name__=="__main__":
    S = 0
    for line in sys.stdin.readlines():
        game_id, rest = line.split(':')
        game_id = int(game_id.split(' ')[1])
        r, g, b = 0, 0, 0
        for draw in rest.split(';'):
            for chunk in draw.split(','):
                balls, colour = chunk.strip().split(' ')
                balls = int(balls)
                if colour == 'red':
                    r = max(r, balls)
                elif colour == 'green':
                    g = max(g, balls)
                elif colour == 'blue':
                    b = max(b, balls)
        S += r*g*b
    print('Sum of power sets is', S)