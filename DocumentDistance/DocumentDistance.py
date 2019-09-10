import numpy as np
from string import maketrans
file=open('./01_input.in','r')

def get_wordscount(file):
    y=[]
    z=[]
    # print(file)
    line1=file.readline()
    while line1:
        inmark=",.-"
        outmark="   "
        mark = maketrans(inmark, outmark)
        line1=line1.translate(mark)
        str1=str(line1)
        #print(str1)
        #print (line1.split(" "))
        #print (str1.split(" "))

        y.extend(str1.split())

        line1 = file.readline()

    #print y
    #print y[2]
    for word in y:

        word=word.lower()
        z.append(word)



    countlist={}
    for word1 in z:
        if word1 in countlist:
            countlist[word1]+=1
        else:
            countlist[word1]=1

    #print countlist
    return countlist





while True:
    filename_1 = file.readline().rstrip()
    filename_2 = file.readline().rstrip()

    if not filename_1 or not filename_2:
        break

    file_1 = open(filename_1,'r')
    file_2 = open(filename_2,'r')









    # Wirite your code here
    # y=[]
    # z=[]
    # print(file_1)
    # line1=file_1.readline()
    # while line1:
    #     str1=str(line1)
    #     #print(str1)
    #     #print (line1.split(" "))
    #     #print (str1.split(" "))
    #
    #     y.extend(str1.split())
    #
    #     line1 = file_1.readline()
    # #print(y)
    # #print y[2]
    # for word in y:
    #     lastchar=word[-1]
    #     if lastchar in [",", ".", "!", "?", ";", "'"]:
    #         word=word[:-1]
    #     #print  word
    #     z.append(word)
    #
    # print z
    #
    # countlist={}
    # for word1 in z:
    #     if word1 in countlist:
    #         countlist[word1]+=1
    #     else:
    #         countlist[word1]=1
    #
    # print countlist

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
    # print wc_key1

    for word in wc2:
        wc_key2[word]=wc2[word]
    # print wc_key2


    # wc3={}
    # for lsw in wc1:
    #     #wc3.keys().extend(lsw)
    #     #print wc3
    #     if lsw in wc2:
    #         wc3[lsw]=wc2[lsw]
    #
    #     else:
    #         wc3[lsw]=0
    #
    # print wc3
    # #wc3.update(wc2)
    # #print wc3
    #
    #
    #
    ts1=np.asanyarray(wc_key1.values())
    ts2=np.asanyarray(wc_key2.values())
    nm1=np.linalg.norm(ts1)
    nm2=np.linalg.norm(ts2)
    mtp=np.dot(ts1,ts2.T)
    #print nm1
    #print nm2
    #print mtp


    rst=mtp/(nm1*nm2)
    #print rst
    rst1=np.arccos(rst)
    print "The distance between the documents is: %0.6f" % rst1


    file_1.close()
    file_2.close()

file.close()


