import json

d = json.load(open('inputs/11.txt'))
print(d)

# walk every object, and if its a digit, add to list
# sum said list
tally = []
def walk(o,ignore=False):
    if type(o) is list:
        for x in o:
            if type(x)==int:
                tally.append(x)
            else:
                walk(x,ignore)
    elif type(o) is dict:
        if 'red' in o.values() and ignore:
            return
        else:
            for k,v in o.items():
                if type(v)==int:
                    tally.append(v)
                else:
                    walk(v,ignore)

for x in d: 
    walk(x)

print(sum(tally))

tally = []
for x in d: 
    walk(x,True)

print(sum(tally))
