#!/usr/bin/env python


import itertools
import math

	
	
	
	
global sie

def flip(n):
    global sie
    sie[n] = (sie[n] + 1) % 2
    return None

def isPrime(n):
    #print n
    if sie[n] == 1:
        return True
    else:
        return False

def aSieve(n):
    res = [2,3,5]       # results list
    global sie
    sie = []
    # initialize sie with 0's for each  i in {6,n}, sie[0] maps to 6
    for i in range(n):
        sie.append(0)
    #print sie
    lim = int(math.floor(math.sqrt(n)))
    for x in range(1,lim):
        for y in range(1,lim):
             m = 4*x*x + y*y
             #print 1, m
             if m <= n and ((m%12 == 1) or (m % 12 == 7)):
                 flip(m)
             m = 3*x*x + y*y
             #print 2, m
             if m <= n and  (m % 12 == 7):
                 flip(m)
             m = 3*x*x -  y*y
             #print 3, m
             if m <= n and x > y and  (m % 12 == 11):
                 flip(m)
##    print sie
##    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    #print lim
    for i in range(5, lim):
        #print i
        if isPrime(i):
            for j in range(n):
                s = j * i * i
                if s > n-1:
                    break
                else:
                    sie[s] = 0

    for i in range(5,n):
        if isPrime(i):
            res.append(i)

    return res

	
	
def replaceDigit (num, digit, place):
	s =  str(num)
	newstr = ""
	for i in range(len(s)):
		if (i == place) :
			newstr += str(digit)
		else:
			newstr += str(s[i])
	return int(newstr)
	

def isValPrime(n):
	if n % 2 == 0:
		return False
	i = 3
	while (i <= math.sqrt(n)):
		if n % i == 0:
			return False
		i += 2
	return True
	
def isEven(n):
	if (n % 2 == 0):
		return True
	return False
	


	
	
	
LIMIT = 10**6

global sieve 
#sieve = aSieve(LIMIT)
print "sieve calculated"

proceed = True
num = 13
while(proceed == True):
	if (not isEven(num)):
		if (isValPrime(num)):
			numLen = len(str(num))
			l = []
			for i in range(numLen):
				l.append(i)
			#print "l is ", l
			for r in range(1,numLen):
				combs = itertools.combinations(l,r)
				for i in combs:
					myCount = 0
					val = i
					lst = []
					#print "val is ", val
					for j in range(10):
						tmpVal = num
						for k in val:
							#print k, "j is", j
							tmpVal = replaceDigit(tmpVal, j, k)	
						#print "tmpval is ", tmpVal	
						lst.append(tmpVal)	
					#if num not in lst:
						#lst.append(num)
					#print lst
					for i in lst:
						if(isValPrime(i)):
							myCount += 1
					if myCount >= 5:
						print "num is ", num, " count is ", myCount
					if myCount >= 8:
						print num
						proceed = False
			#proceed = False
		num += 2
	else :
		num += 2
		
		
		
		
		
		
		