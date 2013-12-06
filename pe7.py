# pe7.py

def isPrime(n):             
    if n in [0,1]:
        return 0
    for i in range(2,n):
        if (n % i == 0):
            return 0
    else:
        return 1

i = 1
q = 3
p = []

while len(p) <10000:
    if isPrime(q) == 1:
        p.append(q)
        i +=1
    q += 2
