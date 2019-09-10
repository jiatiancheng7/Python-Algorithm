# coding=UTF-8
import numpy as np

def max_heapify(arr,n,total):
    lchild=2*n+1
    rchild=2*n+2
    max=n
    if n<=int(total/2):
        if lchild<=total and arr[lchild]>arr[max]:
            max = lchild


        if rchild<=total and arr[rchild]>arr[max]:
            max = rchild
        if max != n:
            temp = arr[n]
            arr[n]=arr[max]
            arr[max]=temp
            max_heapify(arr,max,total)

        # print n
    # print arr
    # max_heapify(arr,n)






if __name__ == "__main__":
    f = open('./03_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        # Write your code here
        # print npyArray
        bg = int(npyArray.size/2) - 1
        #print bg

        while bg != -1:
            max_heapify(npyArray,bg , npyArray.size-1)
            bg-=1
        print "The array representation of the heap is", npyArray
    f.close()



