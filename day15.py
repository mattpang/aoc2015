
# looks like linear programming
from scipy.optimize import linprog
from collections import defaultdict, Counter
from itertools import permutations

d = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

d = open('inputs/15.txt').read()

#  constraints
#  for 2 ingreds x,y
# x and y must be ints
# x+y==100
# maximise total_score  = (x*-1 + y*2) + (x*-2 + y*3) + (x*6 + y*-2) + (x*3 + y*-1) + (x*8 + y*3) 

meta = defaultdict(Counter)
cats = set()
for line in d.splitlines():
    ingredent, stats = line.split(': ')
    for param in stats.split(','):
        spec,score = param.strip().split(' ')
        score = int(score)
        meta[ingredent][spec] = score
        cats.add(spec)

print(meta)
cats.remove('calories')

def calc(part2=False):
    largest_score = 0
    for p in permutations(range(100),len(meta)):
        if sum(p)==100:
            # print(p)
            final_score = 1
            final_scores = [] 
            for param in cats:
                score = 0
                for m,x in zip(meta.keys(),p):
                    score += meta[m][param]*x
                    # print(m,param,x,meta[m][param],meta[m][param]*x)
                # print(param,score)
                if score<0:
                    score = 0 
                final_score *= score
                final_scores.append(score)
            
            if part2:
            # check calories sum to 500
                c_score = 0
                for m,x in zip(meta.keys(),p):
                    c_score += meta[m]['calories']*x
                if c_score == 500:
                    largest_score = max(largest_score,final_score)

            else:
                largest_score = max(largest_score,final_score)
        
    return largest_score

# largest_score = calc(False)
# print(largest_score)
p2_ans = calc(True)
print(p2_ans)