#pe19.py

"""
I first defined the length of each month in a year and leap year.
I then used the variable c to track what was left over at the end of each month.
This starts at one as Mondays are set to one and this was the first day of
January in 1900.

If the "number of days left over from the previous month (i.e. c)" + "number of days in this month"
is divisible by 7 then we know that the next month starts with a Sunday.

"""


# sun = 0, mon = 1, ... , sat = 6

year = [31,28,31,30,31,30,31,31,30,31,30,31]
leapyear = [31,29,31,30,31,30,31,31,30,31,30,]

c = 1
sum = 0
for i in range(1900,2001):
    if i % 4 == 0 and i % 100 != 0:
        for i in leapyear:
            d = (i + c) % 7
            if d == 0:
                sum += 1
            c = d
    elif i % 400 == 0:
        for i in leapyear:
            d = (i + c) % 7
            if d == 0:
                sum += 1
            c = d  
    else:
        for i in year:
            d = (i + c) % 7
            if d == 0:
                sum += 1
            c = d
print sum


"""
# do for 1900
c = 1
sum = 0
for i in year:
    d = (i + c) % 7
    if d == 0:
        sum += 1
    c = d

print sum
 
"""
