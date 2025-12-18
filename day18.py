import copy

d = """##.#.#
...##.
#....#
..#...
#.#..#
####.#
"""
d=open('inputs/18.txt').read()

# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

rgrid = dict()
 
for y,line in enumerate(d.splitlines()):
    gridsize = len(line)

    for x,col in enumerate(line):
        if col == '#':
            rgrid[(x,y)] = True
        else: 
            rgrid[(x,y)] = False
        

blank_grid = dict()
for y in range(0,gridsize):
    for x in range(0,gridsize):
        blank_grid[(x,y)] = False


def run(pt2=False):
    grid = copy.deepcopy(rgrid)
    
    for t in range(0,100):
        new_grid = copy.deepcopy(blank_grid)
        
        for coords, state in grid.items():
            x,y = coords

            neighbours_on = 0
            neighbours_off = 0 

            for j in (-1,0,1):
                for i in (-1,0,1):
                    if not(i==j==0):
                        pos = grid.get((x+i,y+j),None)
                        if pos is True:
                            neighbours_on +=1
                        elif pos is False:
                            neighbours_off += 1
            # if state is False:
            # print(f"{neighbours_on=}, {neighbours_off=}",(x,y))
            
            if state is True and (neighbours_on ==2 or neighbours_on == 3):
                new_grid[(x,y)] = True
            elif state is False and neighbours_on == 3:
                new_grid[(x,y)] = True
            else:
                new_grid[x,y] = False

        grid = new_grid.copy()
        # part 2, corners are always on
        if pt2:
            grid[(0,0)] = True
            grid[(0,gridsize-1)] = True
            grid[(gridsize-1,0)] = True
            grid[(gridsize-1,gridsize-1)] = True

    lights = 0
    lines = [] 
    for y in range(0,gridsize):
        c=''
        for x in range(0,gridsize):
            if grid.get((x,y),None) == True :
                c += '#'
                lights+=1
            else:
                c+='.'
        lines.append(c)
    
    # print('\n'.join(lines))
    return lights

print(run())
print(run(True))