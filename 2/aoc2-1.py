# -*- coding: utf-8 -*-
"""
AOC 2.1

Created on Mon Dec  4 14:25:18 2023

@author: rfoster1
"""
import sys

R, G, B = 12, 13, 14
max_balls_lookup = {'red': R, 'green': G, 'blue': B}

if __name__=="__main__":
    S = 0
    for line in sys.stdin.readlines():
        game_id, rest = line.split(':')
        game_id = int(game_id.split(' ')[1])
        for draw in rest.split(';'):
            for chunk in draw.split(','):
                balls, colour = chunk.strip().split(' ')
                balls = int(balls)
                max_balls = max_balls_lookup[colour]
                if balls > max_balls:
                    S += game_id
                    break
                else: 
                    continue
            else:
                continue
            break
    print('Sum of possible game ids is', game_id*(game_id+1)/2 - S)