import sys
from math import sqrt, floor, ceil

if __name__=="__main__":
    ins = sys.stdin.read()
    times, dists = ins.split('\n')
    _, times = times.split(':')
    times = [int(i) for i in times.split(' ') if i!='']
    _, dists = dists.split(':')
    dists = [int(i) for i in dists.split(' ') if i!='']

    P = 1
    for t, d in zip(times, dists):
        root = sqrt(t*t - 4*d)
        lower = (t-root)/2
        lower =  ceil(lower + 1) if ceil(lower)==lower else ceil(lower) 
        upper = (t+root)/2
        upper = floor(upper-1) if floor(upper)==upper else floor(upper)
        ways = upper - lower + 1
        P *= ways
    print('Product of number of ways', P)

    # P=1
    # for t, d in zip(times, dists):
    #     ways = 0
    #     for hold in range(1, t):
    #         try_dist = hold*(t-hold)
    #         if try_dist > d:
    #             ways += 1
    #     P *= ways
    # print(P)