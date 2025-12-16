# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
from collections import Counter

d = '''turn on 0,0 through 999,999'''
d= '''toggle 0,0 through 999,0'''
d = '''turn off 499,499 through 500,500'''

d = open('inputs/6.txt').read()

grid = Counter()
for line in d.splitlines():
    if line.startswith('turn on '):
        l = line.replace('turn on ','').split(' ')
        op = 1
    elif line.startswith('toggle '):
        l = line.replace('toggle ','').split(' ')
        op = 'flip'
    elif line.startswith('turn off '):
        l = line.replace('turn off ','').split(' ')
        op = 0
    
    x1,y1 = map(int,l[0].split(','))
    x2,y2 = map(int,l[2].split(','))

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if op =='flip':
                if grid[(i,j)] ==0:
                    grid[(i,j)] = 1
                else:
                    grid[(i,j)] = 0
            else:
                grid[(i,j)] = op

print(sum(grid.values()))


grid = Counter()
for line in d.splitlines():
    if line.startswith('turn on '):
        l = line.replace('turn on ','').split(' ')
        op = 1
    elif line.startswith('toggle '):
        l = line.replace('toggle ','').split(' ')
        op = 2
    elif line.startswith('turn off '):
        l = line.replace('turn off ','').split(' ')
        op = -1
    
    x1,y1 = map(int,l[0].split(','))
    x2,y2 = map(int,l[2].split(','))

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            grid[(i,j)] += op
            grid[(i,j)] = max(0,grid[(i,j)])

print(sum(grid.values()))