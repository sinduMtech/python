# Python 3.x code to demonstrate alphabet pyramid pattern
# Function to demonstrate printing alphabets
# initialize lowercase which starts with 97
n1 = 97
# initialize uppercase which starts with 65
n2 = 65
# outer loop to handle number of rows
for i in range(1, 5):
        # check i is even number
        if((i % 2) == 0):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
             for j in range(n1, n1+i):
                if((j % 2) == 1):
                    a = chr(j)
                    print(a, end=""),
                elif((j % 2) == 0):
                    a1 = chr(j)
                    # print the value
                    print (a1.swapcase(), end="")
        # check i is odd number
        elif((i % 2) == 1):
            # inner loop to handle number of columns
            # values changing acc. to outer loop
            for j in range(n2, n2+i):
                if((j % 2) == 1):
                    a = chr(j)
                    print(a, end=""),
                elif((j % 2) == 0):
                    a1 = chr(j)
                    # print the value
                    print (a1.swapcase(), end="")
        print()
