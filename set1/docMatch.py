import numpy as np
import math

def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

def query_creation(query):
    queries=open("queries.txt", "r")
    for line in queries:
        query.append(line.strip())
    return query

def dict_creation(uniqueWords, words):
    for word in words: # loop through the list of words in the line
        if word in uniqueWords: # if the word is already in the dictionary
            uniqueWords[word] = uniqueWords[word] + 1 # count for that word is increased by 1
        else:
            uniqueWords[word] = 1 # otherwise it is added to the dictionary with a count of 1
    return uniqueWords
    
def index_creation(invertedIndex, words, docCount):
    for word in words: # loop through the list of words in the line
        if word not in invertedIndex:
            invertedIndex[word]=[]
            invertedIndex[word].append(1)
            invertedIndex[word].append([docCount])
        else:
            invertedIndex[word][0]+=1
            invertedIndex[word][1].append(docCount)
    return invertedIndex

def search_function(queryWordList):
    temp=[]
    for y in range(0, len(queryWordList)):
        if temp == []:
            if (len(queryWordList)==1) and (queryWordList[y] in invertedIndex):
                exists=True
                temp = invertedIndex[queryWordList[y]][1]
            elif (len(queryWordList)>=2) and (queryWordList[y] in invertedIndex):
                exists = True
                temp = invertedIndex[queryWordList[y]][1]
        elif temp != []:
            if (len(queryWordList)>=3) and (queryWordList[y] in invertedIndex):
                exists = True
                temp=set(temp).intersection(invertedIndex[queryWordList[y]][1])
            if (queryWordList[y] in invertedIndex) and (exists == True):
                exists = True
        if (y==len(queryWordList)-1):
            if (exists == True) and (temp != []):
                match=set(temp).intersection(invertedIndex[queryWordList[y]][1])
                match = " ".join(map(str, match))
    return match

query=[]
uniqueWords = {}
invertedIndex = {}
docCount=0
doc=open("docs.txt", "r")
for line in doc: # reads the file names in the folder
    docCount+=1
    line = " ".join(line.strip().split())
    words = line.split(" ")
    dict_creation(uniqueWords,words)
    index_creation(invertedIndex, words, docCount)

print("Words in dictionary: " + str(len(uniqueWords)))

x=0
query_creation(query)
while x<len(query):
    exists=False
    thisQuery = query[x]
    queryWordList = thisQuery.split()
    print('Query: ' + query[x])
    
    search_function(queryWordList)
    print('Relevant documents: ' + str(search_function(queryWordList)))
    lines_to_read = [int(s) for s in search_function(queryWordList).split() if s.isdigit()]
    lines_to_read =[i-1 for i in lines_to_read]
    doc=open("docs.txt", "r")
    n=0
    vector2=[]
    angles = []
    for line in doc:
        vector1=[]
        vector2=[]
        tempWords={}
        if n in lines_to_read:
            line = " ".join(line.strip().split())
            words = line.split(" ")
            dict_creation(tempWords,words)
            vector1=np.array(list(tempWords.values()))
            for z in range(0,len(queryWordList)):
                i=0
                for y in range(0, len(tempWords)):
                    tempList=list(tempWords.keys())
                    if len(vector2) != len(vector1):
                        if queryWordList[z] == tempList[y] :
                            vector2.append(1)
                        else:
                            vector2.append(0)
                    elif len(vector2) == len(vector1):
                        if (queryWordList[z] == tempList[y]) or (vector2[i]==1) :
                            vector2[i]=1
                    i+=1   
            vector2=np.array(vector2)
            angles.append([(n+1),"{:.2f}".format(calc_angle(vector1,vector2),2)])
        n+=1
    x+=1
    angles=sorted(angles, key = lambda t: t[1])
    for t in range(0, len(angles)):
        print(' '.join(map(str, angles[t])))
    #print('\n'.join(angles))
