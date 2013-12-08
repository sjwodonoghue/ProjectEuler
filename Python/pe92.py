# pe92.py

"""
We first determine how we are going to generate a number chain for a given number
"""
def sumSqrDigits(n):
    sum = 0
    for i in str(n):
        sum += int(i)**2
    return sum

#print sumSqrDigits(1234)
#print sumSqrDigits(745)

"""
A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.
For example,
44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89
"""

def numChain(n):
    i = 1
    l = []
    l.append(n)
    while i < 100:
        l.append(sumSqrDigits(l[i-1]))
        if l[i] == 1 or l[i] == 89:
            return l
        i += 1
        
print numChain(44)
print numChain(89)

def numChainEnd(n):
    i = 1
    l = []
    l.append(n)
    while i < 100:
        l.append(sumSqrDigits(l[i-1]))
        if l[i] == 1 or l[i] == 89:
            return l[i]
        i += 1

"""
Find the number of starting numbers under 10000000 that have a number chain ending in 89.
"""

sum = 0
for i in range(1, 10000000):
    if i % 10000 == 0:
        print i
    if numChainEnd(i) == 89:
        sum += 1

    
print sum



