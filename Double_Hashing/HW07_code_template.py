# coding=UTF-8
import numpy as np

def doublehash(array,n):
    hashtable = []
    for j in  range(len(array)):
        k = int(array[j])
        h1 = k%n
        if(h1 not in hashtable):
            hashtable.append(h1)
        else:
            h2 = (1+(k/n))%(n-1)
            for i in range(n):

                index = (h1+i*h2)%n
                if(index not in hashtable):
                    hashtable.append(index)
                    print "Collision has occurred for element",k,"at position",h1,"finding new Position at position",index
                    break
        if(j == len(array)-1):
            print "Done"


if __name__ == "__main__":
    f = open('./07_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        # Write your code here



        # print(npyArray)
        hash_table = 13

        doublehash(npyArray,hash_table)

    f.close()



