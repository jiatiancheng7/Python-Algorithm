# coding=UTF-8
import numpy as np

def Rabin_Karp_Matcher(Txt, P, d, q):
    q = int(q)
    d = int(d)
    N = len(Txt)
    M = len(P)
    h = pow(d,M-1)%q
    p = 0
    t = 0
    for i in range(M):
        p = (d*p+ord(P[i]))%q
        t = (d*t+ord(Txt[i]))%q
    for j in range(N-M+1):
        if p == t:
            match = True
            for i in range(M):
                if P[i] != Txt[j+i]:
                    match = False
                    break
            if match:
                print 'Pattern found at index',j
        if j < N-M:
            t = (t-h*ord(Txt[j]))%q
            t = (t*d+ord(Txt[j+M]))%q
            t = (t+q)%q
    print 'Done'


if __name__ == "__main__":
    f = open('./06_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.core.defchararray.split(line, sep=",").tolist()
        # Write your code here
        Rabin_Karp_Matcher(npyArray[0],npyArray[1],npyArray[2],npyArray[3])
    f.close()
