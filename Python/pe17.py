#pe17.py

"""
Note that the following is a very messy way to solve this problem and can be greatly refined.


"""

"""
'cardinal words'

'class a numbers' - A
one, two, three, four, five, six, seven, eight, nine,

'class b numbers' - B
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, 

'class c numbers'- C
twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety,

'class d numbers' - D
hundred, thousand

'class E numbers'
numbers 20 - 99 are made up of :

"c" + "a", c in C, a in A, '+' operator corresponds to concatenation

numbers 100 - 999 consist of :

"a" + "hundred" + "and" + {"a" XOR "b" XOR "e"} where e in E
"""

classA = ["one","two","three","four","five","six","seven","eight","nine"]
classB = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
classC = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
classD = ["hundred","thousand"]

# test: generate number words
"""
for i in range(9):
     print classA[i], "\n"

for i in range(10):
    print classB[i], "\n"
"""
"""
for i in range(8):
    for j in range(9):
        print classC[i] + classA[j] 
"""
"""
for i in range(3):
    for j in range(8):
        for k in range(9):
            print classA[i], "hundred and" + classC[j] + classA[k] 
"""

# now to sum the number of letters in the word for each number

sum = 0
# numbers 1 - 9
for i in range(9):
    sum += len(classA[i])

# numbers 10 - 19
for i in range(10):
    sum += len(classB[i])

# numbers 20, 30, 40, ..., 80, 90
for i in range(8):
    sum += len(classC[i])

# numbers 21-29, 31-39, ... , 91-99    
for i in range(8):
    for j in range(9):
        sum +=  len(classC[i]) + len(classA[j])

########### 1-99 done
"""
# numbers 121-129,...,191-199
for i in range(9):
    for j in range(8):
        for k in range(9):
            sum +=  len(classA[i]) + 10 + len(classC[j]) + len(classA[k])
"""
# numbers 101 - 109, 201-209,...901,909
for i in range(9):
    for j in range(9):
        sum += len(classA[i]) + 10 + len(classA[j])
    
# numbers 110 -119, 210-219, ..., 910-919
for i in range(9):
    for j in range(10):
        sum += len(classA[i]) + 10 + len(classB[j])

# numbers 120, 130, ...980, 990
for i in range(9):
    for j in range(8):
        sum += len(classA[i]) + 10 + len(classC[j])

# numbers 121 - 199, 221-299, ..., 921-999
for i in range(9):
    for j in range(8):
        for k in range(9):
            sum += len(classA[i]) + 10 + len(classC[j]) + len(classA[k])

# numbers 100, 200, ..., 900
for i in range (9):
    sum += len(classA[i]) + 7

# number 1000 i.e. "one thousand" and not "thousand"
sum += 11


print sum
