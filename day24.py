from random import shuffle
from math import prod
import copy
import sys
d = open('inputs/24.txt').read()

weights = list(map(int,d.splitlines()))
# weights = [1,2,3,4,5,7,8,9,10,11]
split = sum(weights)//3

# print(split-(sum(weights[-4:])+79+1))

# print(len(weights[-4:]+[79]+[1]))
# part 1 is simple enough to do by hand
print(prod(weights[-4:]+[79]+[1]))

split = sum(weights)//4

cand = weights[-3:]+[53]+[2]

cands = set()
turns = 0

while turns<50000:
    shuffle(weights)
    for i in range(0,9):
        if sum(weights[0:i])==split:
            best = copy.deepcopy(weights[0:i])
            best.sort()
            cands.add(tuple(best))
    turns+=1

lowest_q = sys.maxsize
lowest_len = sys.maxsize

for c in cands:

    if len(c) < lowest_len:
        lowest_len = len(c)
        lowest_q = prod(c)  
    if len(c) == lowest_len:
        if prod(c)<lowest_q:
            lowest_q = prod(c)

print(lowest_q,lowest_len)
