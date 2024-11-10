import re

block_re = '([#\.]+\n)+\n?'

def parse_input():
    ins = open(0).read()
    ins += '\n'
    blocks = []
    for m in re.finditer(block_re, ins):
        block = m.group().strip()
        blocks.append(block)
    return blocks

def b_rows(block):
    rows = []
    for row in block.split('\n'):
        row = row.strip().replace('#', '1').replace('.', '0')
        rows.append(int(row, 2))
    return rows

def b_cols(block):
    rows = [r.strip() for r in block.split('\n')]
    cols = ['' for _ in range(len(rows[0]))]
    for row in rows:
        for r_char, j in zip(row, range(len(cols))):
            cols[j] += r_char
    b_cols = []
    for col in cols:
        col = col.replace('#', '1').replace('.', '0')
        b_cols.append(int(col, 2))
    return b_cols

blocks = parse_input()
Sr = 0
Sc = 0
for b in blocks:
    CR = 0
    rows = b_rows(b)
    L = len(rows)
    for i in range(1, L):
        fr = max(0, i-(L-i))
        to = min(2*i, L)
        xs = [u^v for u, v in zip(rows[fr:i], reversed(rows[i:to]))]
        ps = [(x & (x-1)==0) and x!=0 for x in xs]
        zs = [x==0 for x in xs]
        if sum(ps)==1 and sum(zs)==(len(zs)-1):
            CR = i

    
    CC = 0
    cols = b_cols(b)
    M = len(cols)
    for j in range(1, M):
        fr = max(0, j-(M-j))
        to = min(2*j, M)
        xs = [u^v for u, v in zip(cols[fr:j], reversed(cols[j:to]))]
        ps = [(x & (x-1) == 0) and x!=0 for x in xs]
        zs = [x==0 for x in xs]
        if sum(ps)==1 and sum(zs)==(len(zs)-1):
            CC = j
    
    Sr += CR
    Sc += CC

print(100*Sr + Sc)