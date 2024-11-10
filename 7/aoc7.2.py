import sys
from functools import total_ordering
from collections import Counter

CARDS = 'AKQT98765432J'
CARDS = CARDS[::-1]

FIVEK = 7
FOURK = 6
FULLH = 5
THREK = 4
TWOPR = 3
ONEPR = 2
HIGHC = 1

@total_ordering
class Hand(object):
    def __init__(self, s):
        self.hand = s
        self.vals = tuple(CARDS.find(c) for c in s)
        self.counts = Counter(s)
        nJ = self.counts['J']
        sig = tuple(sorted(self.counts.values()))
        if sig==(5,):
            self._type = FIVEK
        elif sig==(1,4):
            if nJ: self._type = FIVEK
            else: self._type = FOURK
        elif sig==(2,3):
            if nJ==1: self._type = FOURK
            elif nJ==2 or nJ==3: self._type = FIVEK
            else: self._type = FULLH
        elif sig==(1,1,3):
            if nJ: self._type = FOURK
            else: self._type = THREK
        elif sig==(1,2,2):
            if nJ==2: self._type = FOURK
            elif nJ==1: self._type = FULLH
            else: self._type = TWOPR
        elif sig==(1,1,1,2):
            if nJ: self._type = THREK
            else: self._type = ONEPR
        elif sig==(1,1,1,1,1):
            if nJ: self._type = ONEPR
            else: self._type = HIGHC
    
    def __eq__(self, other):
        return self._type==other._type and self.vals==other.vals
    
    def __gt__(self, other):
        if self._type==other._type:
            return self.vals > other.vals
        return self._type > other._type
    
    def __str__(self):
        return self.hand
    
    def __repr__(self):
        return 'Hand({:})'.format(self.hand)


if __name__=="__main__":
    hands = []
    for line in sys.stdin.readlines():
        h, b = line.strip().split(' ')
        hands.append((Hand(h), int(b)))

    hands.sort(key=lambda x: x[0])
    S = sum((i+1)*b for i, (_, b) in zip(range(len(hands)), hands))
    
    print('Winnings', S)