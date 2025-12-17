from itertools import permutations
from collections import defaultdict, Counter, deque

d = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""

d = open("inputs/13.txt").read()

scores = defaultdict(Counter)
names = set()
for line in d.splitlines():
    out = line.split()
    a = out[0]
    b = out[-1][:-1]
    if out[2] == "lose":
        sign = -1
    elif out[2] == "gain":
        sign = 1

    point = sign * int(out[3])

    scores[a][b] = point
    names.add(a)
    names.add(b)

print(names)
largest = 0
for combo in permutations(names):
    rot = deque(combo)
    rot.rotate(1)
    happiness = 0
    for a, b in zip(combo, rot):
        happiness += scores[a][b]
        happiness += scores[b][a]

    if happiness > largest:
        largest = happiness

print(largest)

names.add("me")

largest = 0
for combo in permutations(names):
    rot = deque(combo)
    rot.rotate(1)
    happiness = 0
    for a, b in zip(combo, rot):
        happiness += scores[a][b]
        happiness += scores[b][a]

    if happiness > largest:
        largest = happiness

print(largest)
