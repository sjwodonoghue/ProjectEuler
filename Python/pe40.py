# pe40.py


# Represent the fractional part of the number as a word (as otherwise it is just too long to handle
s = ""
for i in range(1,1000001):
    s += str(i)


# Multiply the requested numbers from the fractional part of the number together to get the
# desired answer.
ans = 1
for i in range(7):
    c = (10**i) - 1
    ans *= int(s[c])
print ans
