CYCLES = 1000000000

def rotate(cols):
    new_cols = ['']*W
    for col in cols:
        for j, c in enumerate(col):
            new_cols[W-j-1] += c
    return new_cols

def calc_weight(grid):
    weight = 0
    for col in grid:
        for i, c in zip(range(W,0,-1),col):
            if c == 'O':
                weight += i
    return weight

def same_grid(A, B):
    for colA, colB in zip(A, B):
        if colA!=colB:
            return False
    return True

def shift_rocks(cols):
    shifted_cols = []
    for col in cols:
        shifted_col = ''
        start = 0
        rocks = 0
        for i, c in enumerate(col):
            if c == 'O':
                rocks += 1
            if c=='#':
                shifted_col += 'O'*rocks + '.'*(i-start-rocks) + '#'
                start = i+1
                rocks = 0
            if i==(W-1):
                if c!='#':
                    shifted_col += 'O'*rocks + '.'*(i-start-rocks+1)
                rocks = 0
        shifted_cols.append(shifted_col)
    return shifted_cols

def parse_input():
    for i, line in enumerate(open(0).readlines()):
        row = line.strip()
        if i==0:
            W = len(row)
            cols = ['']*W
        for j, c in enumerate(row):
            cols[j] += c
    return cols

def transpose(cols):
    rows = ['']*W
    for col in cols:
        for j, c in enumerate(col):
            rows[j] += c
    return rows

def solve(grid, cycles):
    seen_grids = dict()
    for i in range(cycles):
        for orientation in range(4):    
            if orientation==0:
                k = tuple(grid)
                if k in seen_grids.keys():
                    period = i - seen_grids[k]
                    return grid, period, i
                seen_grids[k] = i
            grid = shift_rocks(grid)
            grid = rotate(grid)

grid = parse_input()
W = len(grid)
grid, period, i = solve(grid, CYCLES)
steps_left = (CYCLES - i) % period
for i in range(steps_left):
    for orientation in range(4):
        grid = shift_rocks(grid)
        grid = rotate(grid)
weight = calc_weight(grid)
print(weight)
