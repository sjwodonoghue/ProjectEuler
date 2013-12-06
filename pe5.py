#pe5.py

# What is the smallest number divisible by each of the numbers 1 to 20?



def isPrime(n):             #only  numbers <= 20
    if n in [0,1]:
        return 0
    for i in range(2,n):
        if (n % i == 0):
            return 0
    else:
        return 1
    

# get highest power of a prime under 20
# highest prime factor

def hiPriFact(n):
    if isPrime(n) == 0:
        return 0
    else:
        for i in range(10):
            if (n ** i) > 20:
                return n**(i-1)


ans = 1
for i in range(2,21):
    if isPrime(i) == 1:
        ans = ans * hiPriFact(i)
print ans
