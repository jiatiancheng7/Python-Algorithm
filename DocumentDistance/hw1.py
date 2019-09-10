import numpy as np
from ts1 import get_wordscount
file=open('./01_input.in','r')

while True:
    filename_1 = file.readline().rstrip()
    filename_2 = file.readline().rstrip()

    if not filename_1 or not filename_2:
        break

    file_1 = open(filename_1,'r')
    file_2 = open(filename_2,'r')

    # Wirite your code here

    wc1=get_wordscount(file_1)
    #print wc1

    #print file_2
    wc2=get_wordscount(file_2)
    #print wc2

    wc_key1={}
    wc3=wc1.copy()
    wc3.update(wc2)
    #print wc3


    wc_key1=dict.fromkeys(wc3.keys(),0)
    wc_key2=dict.fromkeys(wc3.keys(),0)
    #print wc_key2

    for word in wc1:
        wc_key1[word]=wc1[word]
    #print wc_key1.values()

    for word in wc2:
        wc_key2[word]=wc2[word]
    #print wc_key2.values()

    ts1=np.asanyarray(wc_key1.values())
    ts2=np.asanyarray(wc_key2.values())
    nm1=np.linalg.norm(ts1)
    nm2=np.linalg.norm(ts2)
    mtp=np.dot(ts1,ts2.T)
    # print nm1
    # print nm2
    # print mtp


    rst=mtp/(nm1*nm2)
    #print rst
    rst1=np.arccos(rst)
    print rst1





    file_1.close()
    file_2.close()

file.close()



