from collections import Counter
def count_visits(x):
    pos = (0,0)
    visited = Counter()
    visited[pos] += 1

    for c in x: 
        match c:
            case 'v':
                new_pos = (pos[0],pos[1]-1)
            case '<':
                new_pos = (pos[0]-1,pos[1])
            case '>':
                new_pos = (pos[0]+1,pos[1])
            case '^':
                new_pos = (pos[0],pos[1]+1)
        visited[new_pos]+=1
        pos = new_pos  
    return len(visited)

def robo_moves(x):
    s_pos = (0,0)
    r_pos = (0,0)
    visited = Counter()
    visited[s_pos] += 1
    visited[r_pos] += 1


    for i,c in enumerate(x):
        if i%2==0:
            # santa moves
            pos = s_pos
        else:
            pos = r_pos

        match c:
            case 'v':
                new_pos = (pos[0],pos[1]-1)
            case '<':
                new_pos = (pos[0]-1,pos[1])
            case '>':
                new_pos = (pos[0]+1,pos[1])
            case '^':
                new_pos = (pos[0],pos[1]+1)
        visited[new_pos]+=1
        
        if i%2==0:
            # santa moves
            s_pos = new_pos
        else:
            r_pos = new_pos

    return len(visited)

assert count_visits('>') == 2
assert count_visits('^>v<') == 4
assert count_visits('^v^v^v^v^v') == 2

ans = count_visits(open('inputs/3.txt').read())
print(ans)

assert robo_moves('^v') == 3
assert robo_moves('^>v<') == 3
assert robo_moves('^v^v^v^v^v') == 11

pt2 = robo_moves(open('inputs/3.txt').read())
print(pt2)
