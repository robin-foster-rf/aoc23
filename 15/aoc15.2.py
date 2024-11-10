from collections import OrderedDict

def hash(s):
    v = 0
    for char in s:
        v += ord(char)
        v = (v*17)%256
    return v

boxes = [OrderedDict() for _ in range(256)]

for line in open(0).read().split(','):
    if line[-1]=='-':
        code = line[:-1]
        H = hash(code)
        if code in boxes[H].keys():
            boxes[H].pop(code)
    else:
        code, val = line.split('=')
        val = int(val)
        H = hash(code)
        boxes[H][code] = val

S = 0
for i, box in enumerate(boxes):
    if box:
        powers = box.values()
        S += (1+i)*sum((j+1)*p for j, p in enumerate(powers))
print('Sum of lens powers', S)