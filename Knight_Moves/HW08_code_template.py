# coding=UTF-8

import numpy as np

class node:
    def __init__(self):
        self.step = None
        self.x = None
        self.y = None

def BFS(xz,yz,ax,ay):
    loc = np.array([[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]],dtype=np.int)
    map1 = np.zeros((8,8),dtype= int)
    list = []
    n = node()
    n.step = 0
    n.x = xz
    n.y = yz
    map1[xz][yz] = 1

    list.append(n)
    while(len(list)):

        h = list.pop(0)

        if(h.x == ax and h.y == ay):
            return h.step
        for i in range(8):

            x = h.x + loc[i][0]
            y = h.y + loc[i][1]

            if (x>=0 and x<=7) and (y>=0 and y<=7) and map1[x][y] == 0:

                map1[x][y] = 1
                t = node()
                t.x = x
                t.y = y
                t.step = h.step + 1
                list.append(t)





if __name__ == "__main__":
    f = open('./08_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        # Write your code here

        x = npyArray[0]
        y = npyArray[1]
        ax = npyArray[2]
        ay = npyArray[3]
        s = BFS(x,y,ax,ay)
        print 'To get from Point(',x,',',y,') to Point(',ax,',',ay,') takes',s,'knight moves.'




    f.close()






