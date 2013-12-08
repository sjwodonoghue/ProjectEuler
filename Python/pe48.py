#pe48.py

sum = 0

for i in range(1,1001):
    sum += i**i


s = str(sum)
t = s[-10:]

print t
