#pe3.py
#Project Euler Problem 3 - 20/08/2011

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math


def isPrime(n):
    k = 0
    for i in range(2,n/2):
        if n % i == 0:                      # if i divides 0 return that n is not prime
            k = 0
            break
        else:  k = 1                         # if i divides n, return that n is a prime
    return k

n = 600851475143L
# find the first prime divisor of n
m = 0
for i in range(2, 1000000):
    if n % i == 0:
        print i
        m = i
        break

# find the second prime divisor of n
j = 0
for i in range(m + 2,100000):
    if n % i == 0:
        print i
        j = i
        break
    else: i = i + 2
    
### now (attempt) to find the largest prime divisor
##j2 = 0
##q = n / (71 * 839)
##for i in range(839,q):
##    s = q - i + 837
##    if  n % s == 0:
##        print s
##        j2 = s
##        break
##    else: i = i + 2
##
##
##q2 = n / (71 * 839 * j2)
##j3 = 0
##for i in range(839,q2):
##    s = q - i + j2 -2
##    if  n % s == 0:
##        print s
##        j3 = s
##        break
##    else: i = i + 2


q = n / (j * m)

# We know that q is odd, so see shall count back in twos from q

for i in range(2,q):
    counter = q - i
    if ((q % counter == 0) and (isPrime(counter) == 1)):
        print counter
        break







    





        

