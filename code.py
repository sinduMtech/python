n1  =   97
n2  =   65
for i in range(1, 5):
    if((i%2)==0):
        for j in range(n1, n1+i):
            if((j%2)==1):
                a = chr(j)
                print a,
            elif((j%2)==0):
                a1 = chr(j)
                print a1.swapcase(),
    elif((i%2)==1):
        for j in range(n2, n2+i):
            if((j%2)==1):
                a = chr(j)
                print a,
            elif((j%2)==0):
                a1 = chr(j)
                print a1.swapcase(),
    print
