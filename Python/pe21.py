#pe21.py

def findDiv(n):
    x = []
    for i in range(1,n):
        if n % i == 0:
            x.append(i)
    return x


def d(n):           #sum of divisors
    x = findDiv(n)
    sum = 0
    for i in x:
        sum = sum + i
    return sum

def isAmicable(n):
    a = d(n)
    b = d(a)
    if d(a) == n and a != n:
        return 1
    else:
        return 0

#print isAmicable(220)

sum = 0

for i in range(1,10001):
    if isAmicable(i) == 1:
        sum = sum + i

print sum
