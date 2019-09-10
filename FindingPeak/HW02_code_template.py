# coding=UTF-8
import numpy as np

def findPeakUtil(arr, left, right, n):

    mid = (left + right)/2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
       (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid


    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, left, (mid - 1), n)


    else:
        return findPeakUtil(arr, (mid + 1), right, n)




if __name__ == "__main__":
    f = open('./02_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        # Write your code here
        #print npyArray
        #print npyArray[0]
        peak=findPeakUtil(npyArray,0,npyArray.size-1,npyArray.size)
        print 'Find it! The peak element is', npyArray[peak]


    f.close()
