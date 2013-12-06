#pe28.py

k = 1001**2

sum = 1
n = 3
while n <= 1001:
    m = n**2
    sum = sum + m + (m - (n-1)) + (m - 2*(n-1)) + (m - 3 * (n-1))

    n = n + 2


print sum 
    
    
    
