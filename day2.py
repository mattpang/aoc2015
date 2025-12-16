d = '''2x3x4
1x1x10'''

d = open('inputs/2.txt').read()

final = 0 
all_ribbons =0 
for line in d.splitlines():
    l,w,h = map(int,line.split('x'))

    total = 2*l*w + 2*w*h + 2*h*l
    smallest = min([l*w,w*h,h*l])
    total += smallest
    final+=total

    bow = l*w*h
    s = sorted([l,w,h])
    
    ribbon = s[0]+s[0]+s[1]+s[1]+bow
    all_ribbons += ribbon

# assert final == 58+43
# assert all_ribbons == 34+14
print(final)
print(all_ribbons)