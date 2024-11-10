import sys
from itertools import cycle
from functools import reduce

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

if __name__=="__main__":
    LRs = sys.stdin.readline().strip()
    nodes = []
    keys = []
    for line in sys.stdin.readlines():
        if line.strip():
            N, rest = line.split(' = ')
            L, R = rest.strip('\n()').split(', ')
            nodes.append((N, (L, R)))
            if N[-1]=='A':
                keys.append(N)

    nodes = dict(nodes)

    # takes far too long to run in parallel checking for simultaneous end Zs. 
    # instead, find independently, then, like the cicadas, find lowest common
    # multiple of the individual chains to find recurrence period. 
    steps = []
    for k in keys:
        s = 0
        for d in cycle(LRs):
            s += 1
            dx = 0 if d=='L' else 1
            next_key = nodes[k][dx]
            if next_key[-1]=='Z':
                break
            else:
                k = next_key
        steps.append(s)
    
    S = reduce(lcm, steps)
    print(S)