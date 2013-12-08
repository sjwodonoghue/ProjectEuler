# pe12.py

import math

# generate n'th triangle number

def triNum(n):
    return (n+1)*n/2

### Find the number of divisors for a number
### Maybe a modified sieve of eratosthenes...
##
### First we try to get the number of powers of a given number that
### divided the number of question. i.e. how many powers of 2 divide
### 100, say
##
### abbreviated from numberPowerDivisors()
### gives the number of powers of m that divide n
##def nPowD(n, m):
##    i = 1
##    if n % m !=0:
##        return 0
##    while n % (m**i) ==0 and (m**1) < n:
##        i +=1
##    return i - 1
##
### sieve of eratosthenes gives the prime divisors of a number
### we just get the number of such divisors, p_i, and sum over
### nPowD(p_i)
##
##
##def sieve(n):
##    l = []
##    p = []
##    for i in range(2,n):
##        l.append(i)
##    for i in l:
##        p.append(i)
##        t = 2
##        while i*t < n:
##            if i*t in l:
##                l.remove(i*t)
##            t +=1
##    return l
##
##print sieve(27)
### get list of prime divisors
### numPriD = numPrimeDivisors
####def numPriD(n):
####    if n in [0,1]:
####        return 0
####    l = []
####    for i in range(2,n+1):
####        l.append(i)
####    for i in l:
##        
##    
##
##
### numD - numDivisors
####def numD(n):

    
"""
Probably don't need the method above

Don't need to get all of the divisors, just need the number of divisors
"""




