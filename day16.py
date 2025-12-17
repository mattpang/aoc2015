from collections import defaultdict

d = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
'''


known = dict()
for line in d.splitlines():
    k,v = line.split(':')
    known[k.strip()] = int(v.strip())


aunts = defaultdict(dict)
aunts_raw = open('inputs/16.txt').read()
for line in aunts_raw.splitlines():
    pos = line.find(':')
    id, counts = line[0:pos], line[pos+1:]

    aid = id.split(' ')[-1]
    for item in counts.split(','):
        k,v = item.split(':')
        aunts[aid][k.strip()] = int(v.strip())

def run(part2:bool=False):
    best_match = None
    best_match_count = 0 
    for k,v in aunts.items():
        n_match = 0 
        for cat,num in v.items():

            if (cat == 'cats' or cat =='trees') and part2:
                if known.get(cat) < num :
                    n_match+=1
                else:
                    break
            elif (cat == 'pomeranians' or cat =='goldfish') and part2:
                if known.get(cat) > num :
                    n_match+=1
                else:
                    break
            else:
                if known.get(cat):
                    if known.get(cat) == num:
                        n_match +=1
            
        if n_match>best_match_count:
            best_match_count = n_match
            best_match = k
    return int(best_match),best_match_count

print(run())
print(run(True))
