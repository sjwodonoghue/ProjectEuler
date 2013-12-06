#pe10.py
import math

def isPrime(n):             
    if n in [0,1]:
        return 0
    if n == 4 or n == 9:
        return 0
    if n == 2:
        return 1
    i = 3
    while i <= int(math.ceil(math.sqrt(n))):
        if (n % i == 0):
            return 0
        i = i + 2
    else:
        return 1


sum = 2
j = 3
while j < 2000000:
    if isPrime(j) == 1:
        print j
        sum = sum + j
    j = j + 2
print sum

