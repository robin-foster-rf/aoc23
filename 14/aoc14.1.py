for i, line in enumerate(open(0).readlines()):
    row = line.strip()
    if i==0:
        W = len(row)
        cols = ['' for _ in range(W)]
    for j, c in enumerate(row):
        cols[j] += c
H = len(cols[0])

S = 0
for col in cols:
    start = 0
    rocks = 0
    for i, c in enumerate(col):
        if c == 'O':
            rocks += 1
        if (c=='#') or (i==(H-1)):
            S += rocks * (2*(H-start)-rocks+1)//2
            start = i+1
            rocks = 0
print('Sum of weights', S)
