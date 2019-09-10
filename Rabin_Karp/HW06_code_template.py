# coding=UTF-8
import numpy as np

def Rabin_Karp_Matcher(Main_String, Sub_String, total, base):
    N = len(Main_String)
    M = len(Sub_String)
    q = total
    d = base

    h = pow(d,M-1)%q
    p = 0
    t = 0
    for i in range(M):
        p = (d*p+ord(Sub_String[i]))%q
        t = (d*t+ord(Main_String[i]))%q
    for j in range(N-M+1):
        if p == t:
            match = True
            for i in range(M):
                if Sub_String[i] != Main_String[j+i]:
                    match = False
                    break
            if match:
                print 'Pattern found at index',j
        if j < N-M:
            t = (t-h*ord(Main_String[j]))%q
            t = (t*d+ord(Main_String[j+M]))%q
            t = (t+q)%q
    print 'Done'

if __name__ == "__main__":
    f = open('./06_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.core.defchararray.split(line, sep=",").tolist()
        # Write your code here
        # print npyArray
        Main_String = npyArray[0]
        Sub_String = npyArray[1]
        total = int(npyArray[2])
        base = int(npyArray[3])
        Rabin_Karp_Matcher(Main_String,Sub_String,total,base)


    f.close()



