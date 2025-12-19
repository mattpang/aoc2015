from collections import Counter

d = open('inputs/23.txt').read()

lines = d.splitlines()

def run(part2=False):
    pos = 0 
    registers = Counter()
    if part2:
        registers['a']=1

    while True:
        if pos <0 or pos>=len(lines):
            break
        line = lines[pos]
        op,val = line.split(' ',maxsplit=1)

        match op: 

            case 'inc':
                registers[val] += 1 
            case 'tpl':
                registers[val] = 3* registers[val]
            case 'hlf':
                registers[val] = registers[val]//2
            case 'jmp':
                v = int(val)
                pos+=v
                continue

            case 'jio':
                reg,v = val.split(', ')
                v = int(v)
                if registers[reg]==1:
                    pos+=v
                    continue
            case 'jie':
                reg,v = val.split(', ')
                v = int(v)
                if registers[reg]%2==0:
                    pos+=v
                    continue
        pos+=1

    print(registers['b'])

run()
run(part2=True)