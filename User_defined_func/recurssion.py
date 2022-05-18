def fun(n): #define a funtion
	if n <= 1:
		return 1
	else:
		return n * fun(n - 1)   # it returns n-1 until the value of n <= 1

a = int(input('Enter a number : '))
print('The factorial : ',fun(a)) # function calling


                            #OR

# lambda function is also a user defined function and it is one line function

fun = lambda n:1 if n <= 1 else n * fun(n - 1) 
a = int(input('Enter a number : '))
print('The factorial : ',fun(a)) # funtion calling
