# pe52.py


def same_digits(n,m):
    if len(str(n)) != len(str(m)):
        return 0
    countern = 0
    counterm = 0
    for i in str(n):
        if i in str(m):
            countern +=1
            continue
        else:
            return 0
    
    for i in str(m):
         if i in str(n):
             counterm +=1
             continue
         else:
            return 0
    if countern == counterm and countern ==len(str(n)):
         return 1

print same_digits(125784,251783)



i = 1
k = 0
while k == 0:
    count = 0
    for j in range(2,7):
        if same_digits(i, j*i) == 1:
            count +=1
    if count == 5:
        print i
        k = 1
    else:
        i+=1 
        
