# pe23.py

import math as m
import time
# get divisors of n

start = time.time()

def div(n):
    l = []
    c = int(m.ceil(m.sqrt(n)))
    for i in range(2,c):
        if n % i == 0:
            l.append(i)
            l.append(n/i)
    l.append(1)
    return l


def sumDiv(n):
    l = div(n)
    sum = 0
    for i in l:
        sum += i
    return sum


def isAb(n):   # isAbundunt
    if sumDiv(n) > n:
        return True
    else:
        return False

def sumAbNum(n):
    sum = 0
    for i in range(1,n):
        if (isAb(i)):
            sum += i
    return sum
# get a list of all the abundunt numbers <= 28123
def abList(n):
    l = []
    for i in range(1,n):
        if (isAb(i)):
            l.append(i)
    return l

# don't need this, can just get sum of sums of two abundant numbers and take away from
# sum(1->n)
# got from stack overflow
def uniq(l):
    result = []
    for x in l:
        if x not in result:
            result.append(x)
    return result

#got from stack overflow
def uniq2(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def abSumSieve(n):
    sum = 0
    nums = abList(n)
    l = []
##    for i in nums:
##        for j in nums:
##            #print i, j
##            if i + j < n:
##                l.append(i+j)
    a = 0
    for i in nums[a:]:
        for j in nums:
            if i + j < n:
                l.append(i+j)
        a += 1
    print max(l)
    print len(l)
    t = uniq2(l)
    print len(t)
    for i in nums:
        if i in t:
            t.remove(i)
    print len(t)
    for i in t:
        sum += i
    return sum


#print abList(28123)
#print abSumSieve(28123)
#print abSum
total = 28123*28124/2
print total - abSumSieve(28123)


print time.time() - start
