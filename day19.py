import re
from random import shuffle

# rules = [('H','HO'),('H','OH'),('O','HH')]
# rules = [('e','H'),('e','O'),('H','HO'),('H','OH'),('O','HH')]
# med = 'HOHOHO'

d = open('inputs/19.txt').read()
lines = d.splitlines()
rules = [] 
for line in lines:
    if '=>' in line:
        a,b = line.split(' => ')
        rules.append((a,b))

med = lines[-1]

bag = set()
for x,v in rules:
    matches = re.finditer(x,med)
    for m in matches:
        new_mole = med[0:m.start()] + v + med[m.end():]
        bag.add(new_mole)

print(len(bag))

target = med
part2 = 0

while target != 'e':
    tmp = target
    for a, b in rules:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = med
        part2 = 0
        shuffle(rules)

print(part2)
