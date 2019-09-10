# coding=UTF-8
import numpy as np

def recursion(n):
    if (n<1):
        return 0
    elif (n<3):
        return 1
    else:
        return recursion(n-1)+recursion(n-2)



if __name__ == "__main__":
    f = open('./10_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line.rstrip(), dtype=int, sep=',')
        # Write your code here
        print recursion(npyArray)


    f.close()

