def which_floor(x) -> int:
    total = 0
    for c in x: 
        if c == '(':
            total+=1
        elif c==')':
            total-=1

    return total

def minus_at(x) -> int:
    total = 0
    for i,c in enumerate(x): 
        if c == '(':
            total+=1
        elif c==')':
            total-=1
        if total==-1:
            break
    return i+1

assert which_floor("(((") == 3
assert which_floor("))(((((") == 3
assert which_floor(")())())") == -3
assert which_floor("))(") == -1

d = open('inputs/1.txt').read()
print(which_floor(d))
assert minus_at('()())') == 5
assert minus_at(')') == 1

print(minus_at(d))