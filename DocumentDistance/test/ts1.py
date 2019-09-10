def get_wordscount(file):
    y=[]
    z=[]
    #print(file)
    line1=file.readline()
    while line1:
        str1=str(line1)
        #print(str1)
        #print (line1.split(" "))
        #print (str1.split(" "))

        y.extend(str1.split())

        line1 = file.readline()
    #print(y)
    #print y[2]
    for word in y:
        lastchar=word[-1]
        if lastchar in [",", ".", "!", "?", ";", "'"]:
            word=word[:-1]
        #print  word
        z.append(word)

    print z

    countlist={}
    for word1 in z:
        if word1 in countlist:
            countlist[word1]+=1
        else:
            countlist[word1]=1

    #print countlist
    return countlist

