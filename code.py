# Python 3.x code to demonstrate alphabets pyramid pattern

# Function to demonstrate printing pyramid pattern
def pyramid(n):
	
	#initialize lowercase which starts with 97
	n1  =   97
	#initialize lowercase which starts with 65
	n2  =   65
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
	    # check i is even number
	    if((i%2)==0):
        
    		# inner loop to handle number of columns
    		# values changing acc. to outer loop
    		for j in range(n1, n1+i):
    		    if((j%2)==1):
    		        a = chr(j)
    		        #print the value
                    print(a),
                elif((j%2)==0):
                    a1 = chr(j)
                    # swap the alphabet into upper to lower or vise versa and print the value
                    print a1.swapcase(),
    	# check i is odd number
	    elif((i%2)==1):
	        
            # inner loop to handle number of columns
    		# values changing acc. to outer loop
            for j in range(n2, n2+i):
                if((j%2)==1):
                    a = chr(j)
                    # print the value
                    print(a),
                elif((j%2)==0):
                    a1 = chr(j)
                    # swap the alphabet into upper to lower or vise versa and print the value
                    print a1.swapcase(),
                    
    		# ending line after each row
    		print("\r")

# Driver Code
n = 4
pyramid(n)
