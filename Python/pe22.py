# pe22.py

import re


f = open('names.txt','r')
s = f.read()

# cannot compile such a string of this size with the re module

# let's find where the commas are, as these separate each name
# the position in s of each of the commas
l = []
for i in range(len(s)):
    if s[i] == ',':
        l.append(i)
print len(l)
# We can now create lists of all of the names

##for a in map(chr, range(65, 91)):
##    names 

##alph = map(chr, range(65, 91))
##for i in range(len(alpha):
##               
def score(name):
    sum = 0
    #alph = map(chr, range(66, 91))
    points = {'A':1}
    for i, v in enumerate(map(chr, range(66, 91))):
        points[v] = i+2
    for s in name:
        sum += points[s] 
    return sum

print score('ALEX')

#print "l ", len(l)
sum = 0
value = 0
for letter in map(chr, range(65, 91)):
    print letter
    names = []
    for i in l:
        if i > 5161:
            break
        elif i == l[0] and s[1] == letter:
            names.append(s[1:i-1])
            #print s[1]
        elif s[l[i-1]+2] == letter:
            names.append(s[l[i-1]+2:l[i] -1])
            #print s[l[i-1]+2:l[i] -1]
    names.sort()
    print len(names)
    nameScores = {}
    for i, name in enumerate(names):
       nameScores[score(name)] = i +1 + value
    for i, j in nameScores.iteritems():
        sum += i*j
    value += len(names)   # number of names starting with the current letter
    #print value
print sum
        
