from functools import lru_cache

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

@lru_cache(maxsize=None)
def propagate(loc, dir, steps):
    if (loc, dir) in visited:
        return 0
    else:
        visited.add((loc, dir))
    steps += 1
    next_loc = (loc[0]+dir[0], loc[1]+dir[1])
    #print(loc, dir)
    if (next_loc[0]<0) or (next_loc[0]>=H) or (next_loc[1]<0) or (next_loc[1]>=W):
        #print('OUT OF BOUNDS')
        return 0
    next_char = rows[next_loc[0]][next_loc[1]]
    if next_char == '|' and dir[1]:
        #print('SPLIT UP/DOWN')
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

S = 0
for i in range(H):
    # left col
    visited = set()
    s = propagate((i,0), (0,1), 0)
    S = max(len(visited), S)
    # right col
    visited = set()
    s = propagate((i,W-1), (0,-1), 0)
    S = max(len(visited), S)
for j in range(W):
    # top row
    visited = set()
    s = propagate((0,j), (1, 0), 0)
    S = max(len(visited), S)
    # bottom row
    visited = set()
    s = propagate((H-1,j), (-1, 0), 0)
    S = max(len(visited), S)

print(S)