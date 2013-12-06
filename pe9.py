#pe9.py



 
for a in range(1,1001):
    for b in range(1,1001):
        for c in range(1,1001):
            f = (a**2) + (b**2)
            g = a + b + c
            if (f == (c**2) and g == 1000):
                print a,
                print b,
                print c,
                print a*b*c
            
