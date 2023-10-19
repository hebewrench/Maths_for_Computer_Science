import numpy as np
import math

def calc_angle(x, y): # function to work out the angle of difference between two vectors
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

def query_creation(query): # function to make a list of the queries from the query text file
    queries=open("queries.txt", "r")
    for line in queries:
        query.append(line.strip()) #removes the endlines from the line
    return query #returns the queries in a list

def dict_creation(uniqueWords, words): # function to create dictionaries
    for word in words: # loop through the list of words in the line
        if word in uniqueWords: # if the word is already in the dictionary
            uniqueWords[word] = uniqueWords[word] + 1 # count for that word is increased by 1
        else:
            uniqueWords[word] = 1 # otherwise it is added to the dictionary with a count of 1
    return uniqueWords

def index_creation(invertedIndex, words, docCount): #function to create the inverted index
    for word in words: # loop through the list of words in the line
        if word not in invertedIndex: #checks if the word is in the index
            invertedIndex[word]=[] #initialises it in the index
            invertedIndex[word].append(1) #sets the initial number of appearances to 1
            invertedIndex[word].append([docCount]) #adds the line number to the index in a list
        else:
            invertedIndex[word][0]+=1 # increases the number of appearances by 1
            invertedIndex[word][1].append(docCount) #adds the line number to the list
    return invertedIndex

def search_function(queryWordList): #function to check if the query word appears in the file
    exists=False
    temp=[]  #empty list to hold the line number
    for y in range(0, len(queryWordList)): #checks for each individual word in the query
        if temp == []: #creates a list of all the documents all words in the query appear in
            if (len(queryWordList)>=1) and (queryWordList[y] in invertedIndex):
                exists=True
                temp = invertedIndex[queryWordList[y]][1] #adds the document numbers to the temp list
        elif temp != []:
            if (len(queryWordList)>=3) and (queryWordList[y] in invertedIndex):
                exists = True
                temp=set(temp).intersection(invertedIndex[queryWordList[y]][1])
                #sets the temp list to only contain documents where all words in the query appear
        if y==len(queryWordList)-1: # length or the list is 1 more than the max index
            if (exists == True) and (temp != []): #checks if there's a list of documents the query appears in
                match=set(temp).intersection(invertedIndex[queryWordList[y]][1])
                #finds the documents that all words in the query appear in
                match = " ".join(map(str, match)) #puts the list in the correct format for output
            if temp == []: #if the query doesn't appear in the file, result is empty
                match = ""
    return match #returns the lines on which the query appears

query=[] #initialising list
uniqueWords = {} #initialising dictionary
invertedIndex = {} #initialising invertedIndex
docCount=0 #initialises the line count
doc=open("docs.txt", "r") #sets the text file to be read
for line in doc: # reads the file names in the folder
    docCount+=1 #increases the line count
    line = " ".join(line.strip().split()) #removes white spaces and endlines
    words = line.split(" ") #checks for additional whitespaces
    dict_creation(uniqueWords,words) #creates the dictionary
    index_creation(invertedIndex, words, docCount) #creates the inverted index

print("Words in dictionary: " + str(len(uniqueWords)))

x=0
query_creation(query) #creates the list of queries
while x<len(query):
    print('Query: ' + query[x]) #outputs the full query
    thisQuery = query[x] #takes the first query
    queryWordList = thisQuery.split() #breaks the query into a list of the individual words
    print('Relevant documents: ' + str(search_function(queryWordList))) # outputs the relevant documents
    lines_to_read = [int(s) for s in search_function(queryWordList).split() if s.isdigit()]
    lines_to_read =[i-1 for i in lines_to_read] #list of the relevant documents, each-1 so the correct document can be read
    doc=open("docs.txt", "r") #opens text document
    n=0 #used to make sure program only searches the relevant documents
    angles = [] #initialises a list for the angles and documents
    for line in doc: #reads through each line in the text file
        vector1=[] #initialises list for the first vector
        vector2=[] #initialises list for the second vector
        tempWords={} #initialises a dictionary to hold the count of each word in the document
        if n in lines_to_read: # if the query is in the document then:
            line = " ".join(line.strip().split()) #standardise the document into a list
            words = line.split(" ") #remove any extra whitespaces
            dict_creation(tempWords,words) #create the temporary dictionary
            vector1=np.array(list(tempWords.values())) #sets the values from this temporary dictionary to the first vector
            for z in range(0,len(queryWordList)):#checks each word in the query
                i=0 #used to make sure every word is checked
                for y in range(0, len(tempWords)): #checks through each word in the document, ignoring repeats
                    tempList=list(tempWords.keys()) # creates a list of each of the words in the document, ignoring repeats
                    if len(vector2) != len(vector1): #checks that the 2nd vector is the right length
                        if queryWordList[z] == tempList[y] : #if the vector's too short, but the query is in the document
                            vector2.append(1) #1 is added to the end of the list
                        else: #if the vector is too short and the query is not in the document
                            vector2.append(0) #0 is added to the end of the list
                    elif len(vector2) == len(vector1): #if the vector is the correct length and either the index is already 1
                        if (queryWordList[z] == tempList[y]) or (vector2[i]==1) : #or the query is in the list at this position
                            vector2[i]=1 #the value is set to 1
                    i+=1 #increments through the indexes of the second vector
            vector2=np.array(vector2) #sets the second vector to the same format as the first
            angles.append([(n+1),"{:.2f}".format(calc_angle(vector1,vector2),2)]) #adds the document number and the angle to 2dp to the angle list
        n+=1 #increments the document line
    x+=1 #increments through the query list
    angles=sorted(angles, key = lambda t: t[1]) #sorts the angles from smallest angle to largest, aka most similar to least
    for t in range(0, len(angles)): #reads through the angle list and for each pair
        print(' '.join(map(str, angles[t]))) #prints it out in the correct format
