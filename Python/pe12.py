#pe12.py


# find primes < n, Sieve of Erateshenes
def sieveErat(n):
    x = []
    for i in range(2,n):
        x.append(i)
    
    for i in range(2,n):
        for k in x:
            #print k
            if k==i or k ==0:
                continue
            elif k % i == 0:
                    x[k-2] = 0
    i = 0
    while i < len(x):
        if x[i] == 0:
            x.pop(i)
        else:
            i +=1
    return x
            

### get multiplicity of a prime divisor of n, i.e. the maximal ineteger k s.t. p**k | n
##def multOfP(n,p):
##    k = 0
##    if n % p != 0:
##        return 0
##    else:
##        for j in range(1,n):
##            if p**j < n and (n % (p**j)) == 0:
##                k = j
##    return k
    

def findDiv(n):
    x = []
    for i in range(2,n):
        x.append(i)
    
    for k in x:
        if n % k != 0:
            x[k-2] = 0

    i = 0
    while i < len(x):
        if x[i] == 0:
            x.pop(i)
        else:
            i +=1
    return x

    

    


