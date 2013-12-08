# pe12_3.py

import time

start = time.time()
# nth trianglenumber
def triNum(n):
    return (n+1)*n/2


# get list of distinct prime divisors of a number n

# sieve of Eratosthenes
# should be replaced with the sieve of atkins

def sieve(n):
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




# list of primes dividing n
def pD(n):
    l = sieve(n)
    plist = []
    for i in l:
        if n % i == 0:
            plist.append(i)
    if len(plist) == 0:
        return [n]
    else:
        return plist


def numpD(n):
    return len(pD(n))

# abbreviated from numberPowerDivisors()
# gives the number of powers of m that divide n
def nPowD(n, m):
    i = 1
    if n % m !=0:
        return 0
    if n == m:
        return 1
    while n % (m**i) ==0 and (m**1) < n:
        i +=1
    return i - 1
       
# get list of the mas i s.t. p**1 | n, we call these a_i

def gen_a_list(n):
    l = pD(n)
    alist = []
    for p in l:
        alist.append(nPowD(n,p))
    return alist

# number of divisors of n
def D(n):
    r = numpD(n)
    #print r
    l = gen_a_list(n)
    #print l
    result = 1
    for i in l:
        result *= i+1
    return result

# now to get number of divisors of a triNum
# want to calculate for n/2 and n+1 or (n+1)/2 and n
# depending on whether n is even or odd

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# num divisors in nth triNum
def Dtn(n):
    if isEven(n) == True:
        return D(n/2) * D(n+1)
    else:
        return D((n+1)/2) * D(n)

i = 2
while len(str(Dtn(i))) < 500:
    print Dtn(i)
    i += 1

print i
print triNum(i)

end = time.time()
print end-start





