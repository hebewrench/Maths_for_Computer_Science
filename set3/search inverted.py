from collections import defaultdict
from operator import itemgetter
import os #allows the program to navigate through the files in the folder

def squish(x): #function for condensing the inverted invertedIndex occurrences
    s=set(x)#https://cs.nyu.edu/courses/spring14/CSCI-UA.0002-002/inverted%20invertedIndex.txt
    return sorted([(i,x.count(i)) for i in s])

uniqueWords = {} # create an empty Dictionary
invertedIndex = {} # initialise the inverted invertedIndex
docCount=0
queryCount=0
query=[]
for doc in os.listdir(): # reads the file names in the folder
    docCount+=1
    if (doc.endswith('.txt')): #only reads the text files
        file = open(doc, "r")
        for line in file: # reads each line in the file
            line = line.strip() # used to remove leading and trailing spaces from the file
            if doc == "queries.txt":
                query.append(line);
            line = " ".join(line.split()) #makes all existing whitespaces, 1 space long
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

print("Words in Dictionary: " + str(len(uniqueWords)))
x=0

while x<len(query):
    exists=False
    thisQuery = query[x]
    print('\nQuery: ' + query[x]+"\n")
    QueryWordList = thisQuery.split()
    print(x)
    for k in invertedIndex:
        if exists == False:
            if len(QueryWordList)>=1:
                if k==QueryWordList[0]:
                    exists = True     
            if len(QueryWordList)>=2:
                if k==QueryWordList[1]:
                    exists = True
        elif exists == True:
            if k==QueryWordList[1]:
                    exists = True
            else:
                exists = False
        if exists == True:
            print(k)
            tuple_list= squish(invertedIndex[k][1])
            relevantDocs = [a_tuple[0] for a_tuple in tuple_list]
            relDocs = ' '.join(map(str, relevantDocs))
            print('Relevant Documents: ' + relDocs)
        exists = False
    x+=1
