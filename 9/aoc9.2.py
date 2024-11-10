import sys
from functools import reduce

if __name__=="__main__":
    seqs = []
    for line in sys.stdin.readlines():
        seqs.append(list(int(i) for i in line.strip().split(' ') if i!=''))

    S = 0
    for seq in seqs:
        done = False
        stack = []
        while not done:
            diff = [b-a for a, b in zip(seq, seq[1:])]
            stack.append(seq[0])
            if all(d==0 for d in diff):
                done = True
            seq = diff
        S += reduce(lambda x, y: y-x, reversed(stack))
    print('Sum', S)
