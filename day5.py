
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
from collections import Counter
import re 

def is_nice(x):
    vowel_count = Counter()
    double = False
    if 'ab' in x or 'cd' in x or 'pq' in x or 'xy' in x:
        return False
    prev = None
    for c in x:
        vowel_count[c]+=1
        if prev:
            if c==prev:
                double=True
        prev = c

    
    if (sum([vowel_count[i] for i in 'aeiou']) >=3) and double:
        return True
    
    return False

assert is_nice('ugknbfddgicrmopn') == True
assert is_nice('aaa') == True
assert is_nice('jchzalrnumimnmhp') == False
assert is_nice('haegwjzuvuyypxyu') == False
assert is_nice('dvszwmarrgswjxmb') == False

print(sum([is_nice(i) for i in open('inputs/5.txt').read().splitlines()]))


def is_nice_v2(x):
    # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    rule1 = False
    rule2 = False

    pairs = [x+y for x,y in zip(x,x[1:])]
    for p in pairs:
        ans = [m.start() for m in re.finditer(p,x)]
        if len(ans) >= 2:
            last = None
            for a in ans:
                if last is not None:
                    if (a - last) >1:
                        rule1 = True
                last = a
        

    for a,b,c in zip(x,x[1:],x[2:]):
        if a==c:
            rule2 = True

    return rule1 and rule2

assert is_nice_v2('qjhvhtzxzqqjkmpb') == True
assert is_nice_v2('xxyxx') == True
assert is_nice_v2('uurcxstgmygtbstg') == False
assert is_nice_v2('ieodomkazucvgmuy') == False

print(sum([is_nice_v2(i) for i in open('inputs/5.txt').read().splitlines()]))
