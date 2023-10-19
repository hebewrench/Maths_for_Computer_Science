import numpy as np
import math
import itertools

def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

#query location
query=[]
queries=open("queries.txt", "r")
for line in queries:
    query.append(line.strip())
#end query searching

#dictionary and invertedindex creation
uniqueWords = {} # create an empty Dictionary
invertedIndex = {} # initialise the inverted index
docCount=0
doc=open("docs.txt", "r")
for line in doc: # reads the file names in the folder
    temp =[]
    docCount+=1
    line = " ".join(line.strip().split())
    words = line.split(" ")
    for word in words: # loop through the list of words in the line
        if word in uniqueWords: # if the word is already in the dictionary
            uniqueWords[word] = uniqueWords[word] + 1 # count for that word is increased by 1
        else:
            uniqueWords[word] = 1 # otherwise it is added to the dictionary with a count of 1

        if word not in invertedIndex:
            invertedIndex[word]=[]
            invertedIndex[word].append(1)
            invertedIndex[word].append([docCount])
        else:
            invertedIndex[word][0]+=1
            invertedIndex[word][1].append(docCount)
#end creation


print("Words in Dictionary: " + str(len(uniqueWords)))

#search function
x=0
while x<len(query):
    exists=False
    thisQuery = query[x]
    queryWordList = thisQuery.split()
    print('Query: ' + query[x])
    temp=[]
    for y in range(0, len(queryWordList)):
        if temp == []:
            if (len(queryWordList)==1) and (queryWordList[y] in invertedIndex):
                exists=True
                temp = invertedIndex[queryWordList[y]][1]
            elif (len(queryWordList)==2) and (queryWordList[y] in invertedIndex):
                exists = True
                temp = invertedIndex[queryWordList[y]][1]
            elif (len(queryWordList)==3) and (queryWordList[y] in invertedIndex):
                exists = True
                temp = invertedIndex[queryWordList[y]][1]

        elif temp != []:
            if (len(queryWordList)==3) and (queryWordList[y] in invertedIndex):
                exists = True
                temp=set(temp).intersection(invertedIndex[queryWordList[y]][1])
            if (queryWordList[y] in invertedIndex) and (exists == True):
                exists = True

        if (y==len(queryWordList)-1):
            if (exists == True) and (temp != []):
                match=set(temp).intersection(invertedIndex[queryWordList[y]][1])
                match = " ".join(map(str, match))
                print('Relevant Documents: ' + str(match))
                
    lines_to_read = [int(s) for s in match.split() if s.isdigit()]
    lines_to_read =[i-1 for i in lines_to_read]
    doc=open("docs.txt")
    n=0
    for line in doc:
        if n in lines_to_read:
            testVect1=[]
            testDict={}
            testVect2=[]
            line = " ".join(line.strip().split())
            words = line.split(" ")
            for word in words:
                if word in queryWordList:
                    testVect1.append(1)
                else :
                    testVect1.append(0)
                if word in testDict: # if the word is already in the dictionary
                    testDict[word] = testDict[word] + 1 # count for that word is increased by 1
                    testVect2.append(testDict[word])
                else:
                    testDict[word] = 1
                    testVect2.append(testDict[word])
            print(testVect1)
            print(testVect2)
            print(str(n+1), calc_angle(testVect1,testVect2))
            n+=1
        else:
            n+=1
    print("\n")
    x+=1
