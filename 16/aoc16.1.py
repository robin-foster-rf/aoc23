from collections import defaultdict
import sys

# def parse_input():
#     optics = dict()
#     for i, line in enumerate(open(0).readlines()):
#         for j, c in enumerate(line):
#             if c in '|\\-/':
#                 optics[(i,j)] = c
#     H = i+1
#     W = j+1
#     print(H,W)
#     rows = [[] for _ in range(H)]
#     cols = [[] for _ in range(W)]
#     for k, v in optics.items():
#         print(k,v)
#         if v == '|':
#             a = 2
#         elif v == '/':
#             a = -1
#         elif v == '\\':
#             a = +1
#         rows[k[0]].append((k[1],a))
#         if v == '-':
#             a = 2
#         elif v == '/':
#             a = +1
#         elif v == '\\':
#             a = -1
#         print(k,v,a)
#         cols[k[1]].append((k[0],a))
#     return optics, rows, cols

# def propagate(loc, dir):
#     if dir[0]: # travelling horizontally
#         if dir[0]==-1: # to the left
#             optics = reversed([op for op in ROWS[loc[0]] if op[1]<loc[1]])
#         else:
#             optics = [op for op in ROWS[loc[0]] if op[1]>loc[1]]
#             for j in range(loc[1])
#     elif dir[1]: # travelling vertically
#         pass

def parse_input():
    rows = []
    for line in open(0).readlines():
        rows.append(line.strip())
    H = len(rows)
    W = len(rows[0])
    cols = ['' for _ in range(H)]
    for row in rows:
        for i, ch in enumerate(row):
            cols[i] += ch
    return rows, cols, H, W

def propagate(loc, dir, steps):
    if (loc, dir) in visited.keys():
        return 0
    else:
        visited[(loc, dir)] += 1
    steps += 1
    next_loc = (loc[0]+dir[0], loc[1]+dir[1])
    print(loc, dir)
    if (next_loc[0]<0) or (next_loc[0]>=H) or (next_loc[1]<0) or (next_loc[1]>=W):
        #print('OUT OF BOUNDS')
        return 0
    next_char = rows[next_loc[0]][next_loc[1]]
    if next_char == '|' and dir[1]:
        print('SPLIT UP/DOWN')
        steps += propagate(next_loc, (-1, 0), steps)
        steps += propagate(next_loc, (+1, 0), steps)
    elif next_char == '/':
        #print('REFLECT')
        if dir[1]==1:
            next_dir = (-1,0)
        elif dir[1]==-1:
            next_dir = (+1,0)
        elif dir[0]==1:
            next_dir = (0,-1)
        elif dir[0]==-1:
            next_dir = (0,+1)
        else:
            next_dir = dir
        steps += propagate(next_loc, next_dir, steps)
    elif next_char == '\\':
        #print('REFLECT')
        if dir[1]==1:
            next_dir = (+1,0)
        elif dir[1]==-1:
            next_dir = (-1,0) 
        elif dir[0]==1:
            next_dir = (0,+1)
        elif dir[0]==-1:
            next_dir = (0,-1)
        else:
            next_dir = dir
        steps += propagate(next_loc, next_dir, steps)
    elif next_char == '-' and dir[0]:
        #print('SPLIT LEFT/RIGHT')
        steps += propagate(next_loc, (0, -1), steps)
        steps += propagate(next_loc, (0, +1), steps)
    else:
        #print('CONTINUE')
        steps += propagate(next_loc, dir, steps)
    return steps


rows, cols, H, W = parse_input()
visited = defaultdict(lambda : 0)

sys.setrecursionlimit(H*W) 
# hmm, this seems maybe not great to fiddle with. but,, it doesn't actually 
# break, so... 
S = propagate((0,0), (0,1), 0)

V = set(k[0] for k in visited.keys())
S = len(V)
print(S)