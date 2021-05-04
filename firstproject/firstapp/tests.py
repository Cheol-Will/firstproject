from django.test import TestCase
text = "나는 나는 케로케로 케로케로"

testlist = text.split()

print(testlist)

worddict = {}

for word in testlist:
    if word in worddict:
        worddict[word] += 1
    else:
        worddict[word] = 1

print(worddict)