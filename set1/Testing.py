file = open("docs.txt", "r")
string = file.read()
docs = string.split()

def BuildDictionary(docs):
    Dictionary = {}
    for item in range(len(docs)):
        if docs[item] not in Dictionary:
            Dictionary[docs[item]] = item
    return Dictionary

dic = BuildDictionary(docs)

string = file.read()


import collections

"""
inverted_index = collections.defaultdict(set)
for line in file:
    document = line.strip()
    for word in document:
        inverted_index[word].add(document)
print(len(inverted_index))"""
"""

inverted_index = collections.defaultdict(set)
lines = string.strip()
for word in lines:
    inverted_index[word].add(lines)
print(len(inverted_index))
"""

invertedIndex = defaultdict(list)
for idx, text in enumerate(docs):
    for word in text:
        invertedIndex[word].append(idx)
"""
invertedIndex = {i:[] for i in dic}
for word in dic:
    for i in range(len(array)):
        if word in array[i]:
            invertedIndex[word].append(i)"""
print(len(invertedIndex("computer")))
