# coding=UTF-8
import numpy as np

MAX_value = 999999

def dijkstra(graph, s):
    if graph is None:
        return None
    dist = [MAX_value]*len(graph)
    dist[s] = 0
    S = []
    Q = [i for i in range(len(graph))]
    dist_init = [i for i in graph[s]]
    while Q:
        u_dist = min([d for v, d in enumerate(dist_init) if v in Q])
        u = dist_init.index(u_dist)

        S.append(u)
        Q.remove(u)

        for v, d in enumerate(graph[u]):
            if 0 < d < MAX_value:
                if dist[v] > dist[u]+d:
                    dist[v] = dist[u]+d
                    dist_init[v] = dist[v]
    return dist






if __name__ == "__main__":
    f = open('./09_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.core.defchararray.split(line.rstrip(), sep=",").tolist()
        # Write your code here
        #print ord(npyArray[0])-64

        maxnum =  ord(max(npyArray))-64
        # print maxnum
        graph_1 = np.full((maxnum,maxnum),MAX_value,dtype=np.int)
        for j in range(maxnum):
            graph_1[j][j] = 0
        # print graph_1

        for i in range(len(npyArray)/3):
            start = npyArray[i*3+0]
            stop = npyArray[i*3+1]
            weight = npyArray[i*3+2]


            # print start,stop,weight

            x1 = ord(start)-65
            x2 = ord(stop)-65
            # print  x1,x2
            graph_1[x1][x2] = weight
            # graph_1[x1][x2] = weight
        # print graph_1




        distance = dijkstra(graph_1, 0)

        fin = ord(npyArray[-1])-65
        fin_ans = distance[fin]
        print "The shortest distance from A to",npyArray[-1],"is",fin_ans

    f.close()






