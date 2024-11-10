import sys

PIPE_CHARS = '|-LJ7F'

def tri(a, b):
    return ( a[0]*b[1] - a[1]*b[0] ) / 2

def subtr(a, b):
    return tuple(x-y for x, y in zip(a, b))

if __name__=="__main__":
    ins = sys.stdin.read()
    rows = ins.split('\n')

    # find start point
    for i, row in enumerate(rows):
        j = row.find('S')
        if j>-1:
            break
    start = (i, j)
    
    # find first steps
    Ts = [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]
    Cs = [rows[i][j] for i, j in Ts]
    possible_Cs = ['-J7', '|JL', '_FL', '|7F']
    TTs = []
    for T, C, pC in zip(Ts, Cs, possible_Cs):
        if C in pC:
            TTs.append(T)
    
    left, right = TTs
    
    # calculate area using cross product of adjacent line segments. 
    # this gives oriented area so negative if curving one way, positive if 
    # curving the other. 
    # Need to correct by subtracting one half of the edge. Keep track with B
    A = 0
    S = 0
    B = 0
    pos = left
    hdg = tuple(x-y for x, y in zip(pos, start))

    A += tri(start, pos)
    S += 1
    if hdg in ((0,1), (1,0)):
        B += 1
    print('start', start, hdg, '', S, A)
    while pos != start:
        i, j = pos
        C = rows[i][j]
        if C in '|-':
            pass # no need to change heading
        elif C=='L':
            if hdg==(1, 0): hdg = (0, 1)
            elif hdg==(0, -1): hdg = (-1, 0)
        elif C=='J':
            if hdg==(1, 0): hdg = (0, -1)
            elif hdg==(0, 1): hdg = (-1, 0)
        elif C == '7':
            if hdg==(0, 1): hdg = (1, 0)
            elif hdg==(-1, 0): hdg = (0, -1)
        elif C == 'F':
            if hdg==(-1, 0): hdg = (0, 1)
            elif hdg==(0, -1): hdg = (1, 0)
            
        next_pos = tuple(x+y for x, y in zip(pos, hdg))
        A += tri(pos, next_pos)
        S += 1
        if hdg in ((0,1), (1,0)):
            B += 1
        pos = next_pos
        #print('{:}\t{:}\t{:}\t{:}\t{:}'.format(pos, hdg, C, S, A))
    A = abs(A) - B + 1
    print('Area', A, 'Steps', S, B)