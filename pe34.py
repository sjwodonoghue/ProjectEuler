# pe34.py

import math



def  sumFactDigits(n):
    l = []      #list  0!-9!
    for i in range(10):
        l.append(math.factorial(i))
    sum = 0
    for i in str(n):
        sum += l[int(i)]
    return sum



# Get an upper bound for these "curious" numbers, which exists as (Sum(di)(i=1,...,n)) < 10**n as n -> inf.

def maxSumFactDigits(n):        # n = number of digits in n, i.e. length of n
    return sumFactDigits((10**n) -1)

def maxDigit(n):
    for i in range(10):
        if math.factorial(i) > n:
            return i

def maxSFDCons(n):           # constrained
    l = []
    if maxDigit(n) == None:
        return None
    for i in range(maxDigit(n),10):
        l.append(i)
    return l
print maxDigit(33334)
print maxSFDCons(33334) 


def alpha(n):
    l = []      #list  0!-9!
    for i in range(10):
        l.append(len(str(math.factorial(i))))
    sum = 0 
    for i in str(n):
        sum += l[int(i)]
    #print sum
    if sum > len(str(n)):
        return 0
    else:
        return 1

#print alpha(33333)
print sumFactDigits(33334)

sum1 = 0
l = 0
for j in range(10):
    for i in range(10**j,10**(j+1)):
       #print i
       if alpha(i) == 0:
           continue
       if maxSFDCons(10**(j+1)) == None:
           continue
       for k in str(i):
           if int(k) in maxSFDCons(10**(j+1)):
                l +=1
       if l > 0:
            l = 0
            continue
       if sumFactDigits(i) == i:
            sum1 += i
       print i    
print sum1

