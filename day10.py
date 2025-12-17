def run(x):
    seen = 0
    p = x[0]
    ans = ''
    for c in x:
        if c==p:
            seen+=1
        else:
            ans += str(seen)
            ans += p
            p=c
            seen=1
    
    p=c
    ans += str(seen)
    ans += p

    return ans

assert run('1') == '11'
assert run('11') == '21'
assert run('21') == '1211'
assert run('1211') == '111221'
assert run('111221') == '312211'

out = run('1321131112')
for i in range(49):
    out = run(out)
print(len(out))