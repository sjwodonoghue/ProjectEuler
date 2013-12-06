# pe30.py

inf = 5* (2**5)
sup = 5 * (10**5)

count = 0
l = []
for i in range(inf,sup):
    # now sum the fifth powers of each of the digits
    sum = 0
    for j in str(i):
        sum += int(j)**5

    if i == sum:
        l.append(i)
        count += 1
        
ans = 0
for i in l:
    ans += i


print "The numbers are: ", l
print "There are ", count, " such numbers."
print "Sum of the numbers is ", ans, "."



