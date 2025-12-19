target_y,target_x = 2981, 3075
# target_y,target_x = 5,5
code = dict()
# pos = 1
pos = 20151125
i=1
while True:
    # code[1,1] = 20151125
    for x in range(1,i,1):
        # y is the count down. 
        y = i-x
        # print(pos,y,x)
        # pos+=1
        if target_y==y and target_x == x:
            print(pos)
            exit()
        pos = (pos*252533 % 33554393)
    i+=1