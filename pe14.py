#pe14.py

def runSeq(n):
    x = []
    x.append(n)
    if n ==1:
        return 4

    else:
        while n != 1:
            if ((n % 2) == 0):
                n = n/2
                #print n
                x.append(n)
            else:
                n = (3*n) +1
                #print n
                x.append(n)

        return len(x)


y = [0,0]

for i in range(1,1000001):
    if runSeq(i) > y[0]:
        y[0] = runSeq(i)
        y[1] = i
        print y[0], ",  ", y[1]
print y
            
                
