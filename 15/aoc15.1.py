def hash(s):
    v = 0
    for char in s:
        v += ord(char)
        v = (v*17)%256
    return v

S = 0
for line in open(0).read().split(','):
    S += hash(line)
    
print('Sum of hashes', S)