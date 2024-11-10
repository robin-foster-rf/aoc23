import sys
from itertools import cycle

if __name__=="__main__":
    LRs = sys.stdin.readline().strip()
    nodes = []
    for line in sys.stdin.readlines():
        if line.strip():
            N, rest = line.split(' = ')
            L, R = rest.strip('\n()').split(', ')
            nodes.append((N, (L, R)))

    nodes = dict(nodes)

    key = 'AAA'
    steps = 0
    for d in cycle(LRs):
        steps += 1
        key = nodes[key][0] if d=='L' else nodes[key][1]
        if key=='ZZZ':
            break
    print('Steps', steps)