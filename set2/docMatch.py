import numpy as np
import math
import itertools

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

def dict_and_index_creation(uniqueWords,invertedIndex):
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

def squish(x):
    s=set(x)
    return sorted([(i,x.count(i)) for i in s], key=first)


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
            """    
            elif (len(queryWordList)==3) and (queryWordList[y] in invertedIndex):
                exists = True
                temp = invertedIndex[queryWordList[y]][1]
            elif (len(queryWordList)==4) and (queryWordList[y] in invertedIndex):
                exists = True
                temp = invertedIndex[queryWordList[y]][1]
            """
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
uniqueWords = {} # create an empty Dictionary
invertedIndex = {} # initialise the inverted index

dict_and_index_creation(uniqueWords,invertedIndex)
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
    #lines_to_read =[i-1 for i in lines_to_read]
    #print(lines_to_read)
    doc=open("docs.txt")
    
    x+=1
    vector3=[]
    for n in list(invertedIndex.values()):
        q="".join(str(n[1]))
        print(search_function(queryWordList))
        print(q)
        if search_function(queryWordList) in q:
            vector3.append(lines_to_read)
            
            
    print("this vector: ")
    print(vector3)

vector1=np.array([1, 2, 2, 1, 2, 1, 2])
vector2=np.array([0, 0, 1, 0, 0, 0, 0])

print(calc_angle(vector1,vector2))


    
