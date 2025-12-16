# traveling salesman / santa. try to do dykstras take the
# shortest leg of each node to the next
from collections import defaultdict
from itertools import permutations

d = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

d = open("inputs/9.txt").read()

legs = defaultdict(dict)
cities = set()
visited = set()

for line in d.splitlines():
    s, _, t, _, dist = line.split(" ")
    dist = int(dist)

    legs[s][t] = dist
    legs[t][s] = dist

    cities.add(s)
    cities.add(t)

tally = 0
smallest = 1E10
largest = 0 

for route in permutations(cities):
    tally = 0 
    for a,b in zip(route,route[1:]):
        tally+=legs[a][b]
    if tally>largest:
        largest = tally
    if tally<smallest:
        smallest=tally

print(smallest)
print(largest)
