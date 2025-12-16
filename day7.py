from functools import cache
d = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

d=open('inputs/7.txt').read()
sinks = dict()
for line in d.splitlines():
    ops , target = line.split('-> ')
    x = op = y = None
    sinks[target] = ops

registers = dict()
# need to do a topological sort to rearrange the starting lines order, only then can the program be run in the correct order. 

@cache
def get_value(t)->int:
    if t.isdigit():
        return int(t)
    ops = sinks[t]
    out = ops.strip().split(' ')
    if len(out)==3:
        x,op,y = out

    elif len(out) == 2:
        op, x = out

    elif len(out) == 1:
        x = out[0]
        if x.isdigit():
            registers[target] = int(x)
            return int(x)
        else:
            print('line',line)
            return get_value(x)
        
    match op:
        case 'AND':
            return get_value(x) & get_value(y) & 0xffff
        case 'OR':
            return get_value(x) | get_value(y) & 0xffff
        case 'LSHIFT':
            return get_value(x) << int(y) & 0xffff
        case 'RSHIFT':
            return get_value(x) >> int(y) & 0xffff
        case 'NOT':
            # should be 16 bit unary NOT. 
            return ~get_value(x) & 0xffff
        case _:
            print(f'no match {line=} {op=} {x=} {y=}')
    

# print(get_value('b'))
# print(get_value('n'))
signal = get_value('a')
print(signal)

# part 2. overwrite b to a
sinks['b'] = str(signal)
get_value.cache_clear()
new_signal = get_value('a')
print(new_signal)