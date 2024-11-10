import sys
from math import sqrt, floor, ceil

if __name__=="__main__":
    ins = sys.stdin.read()
    time, dist = ins.split('\n')
    _, time = time.split(':')
    t = int(time.replace(' ', '').strip())
    _, dist = dist.split(':')
    d = int(dist.replace(' ', '').strip())

    root = sqrt(t*t - 4*d)
    lower = (t-root)/2
    lower =  ceil(lower + 1) if ceil(lower)==lower else ceil(lower) 
    upper = (t+root)/2
    upper = floor(upper-1) if floor(upper)==upper else floor(upper)
    ways = upper - lower + 1

    print('Number of ways', ways)