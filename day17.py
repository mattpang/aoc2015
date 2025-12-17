from itertools import combinations
from collections import Counter
d = """20
15
10
5
5
"""
d = open('inputs/17.txt').read()

boxes = [int(x) for x in d.splitlines()]

i=0
target = 150 
count = 0
combos = Counter()
for i in range(len(boxes)):
    for p in combinations(boxes,i):
        if sum(p) == target:
            count+=1
            combos[len(p)] +=1
            

print(count)
mink = min(combos.keys())
print(combos[mink])