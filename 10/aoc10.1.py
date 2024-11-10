import sys

PIPE_CHARS = '|-LJ7F'

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

    S = 0
    left, right = TTs
    left_hdg = tuple(x-y for x, y in zip(left, start))
    right_hdg = tuple(x-y for x, y in zip(right, start))
    while left != right:
        hdg = left_hdg
        pos = left
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
        pos = tuple(x+y for x, y in zip(pos, hdg))
        left = pos
        left_hdg = hdg
        leftC = C

        hdg = right_hdg
        pos = right
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
        pos = tuple(x+y for x, y in zip(pos, hdg))
        right = pos
        right_hdg = hdg
        rightC = C

        S += 1
        #print('left\t', left, left_hdg, leftC, '\tright\t', right, right_hdg, rightC, '\t', S)
    print('Steps', S+1)