#pe20.py


import math

s = str(math.factorial(100))

sum = 0
for i in range(len(s)):
    sum += int(s[i])

print sum
