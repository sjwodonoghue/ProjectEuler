#!/usr/bin/env python

from itertools import permutations




def eSieve(n):          # Sieve of Eratosthenes, returns all primes <= n
    l = []
    p = []
    for i in range(2,n):
        l.append(i)
    for i in l:
        p.append(i)
        t = 2
        while i*t < n:
            if i*t in l:
                l.remove(i*t)
            t +=1
    return l
	

def isSeq(n1, n2, n3):
	l1 = int2Lst(n1)
	l2 = int2Lst(n2)
	l3 = int2Lst(n3)
	return (l1 == l2) & (l1 == l3) & (l2 == l3)
	
def int2Lst(n):
	s = str(n)
	l = []
	for i in range(len(s)):
		l.append(s[i])
	l.sort()
	return l
					

l2 = eSieve(10000)
l = []
for i in l2:
	if i > 1000:
		l.append(i)
print l

newList = []

for i in range(len(l)):
	print l[i]
	for k in range(len(l[i:])):
		for j in range(len(l[k:])):
			if isSeq(l[i], l[j], l[k]) & ((l[k] - l[j]) == (l[j] - l[i])) & (l[i] != l[k]) & (l[k] != l[j]):
				print l[i], l[j], l[k]
				newList.append([l[i], l[j], l[k]])



print newList

	