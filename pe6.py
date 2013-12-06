#pe6.py



def isPrime(n):             
    if n in [0,1]:
        return 0
    for i in range(2,n):
        if (n % i == 0):
            return 0
    else:
        return 1
