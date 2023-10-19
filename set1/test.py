def dict_creation(uniqueWords, words):
    for word in words: # loop through the list of words in the line
        if word in uniqueWords: # if the word is already in the dictionary
            uniqueWords[word] = uniqueWords[word] + 1 # count for that word is increased by 1
        else:
            uniqueWords[word] = 1 # otherwise it is added to the dictionary with a count of 1

def index_creation(invertedIndex, words):
    for word in words: # loop through the list of words in the line
        if word not in invertedIndex:
            invertedIndex[word]=[]
            invertedIndex[word].append(1)
            invertedIndex[word].append([docCount])
        else:
            invertedIndex[word][0]+=1
            invertedIndex[word][1].append(docCount)

uniqueWords = {}
invertedIndex = {}
docCount=0
doc=open("docs.txt", "r")
for line in doc: # reads the file names in the folder
    temp =[]
    docCount+=1
    line = " ".join(line.strip().split())
    words = line.split(" ")
    dict_creation(uniqueWords,words)
    index_creation(invertedIndex, words)

print("Words in dictionary: " + str(len(uniqueWords)))
print(uniqueWords)
print(invertedIndex)

