from numpy import*                              # importing module
r,c = map(int,input('Enter row and column : ').split())
a = eye(r,c)                 # using eye funtion it creates diagonal elements 1 and other elements 0, it takes two input row and column
print('The array is \n',a)


	#OR

from numpy import*            # importing module
a = []                        # declaring list 
r,c = map(int,input('Enter row and column : ').split())
for i in range(r):
	for j in range(c):
		if i == j:
			a.append(1.0)
		else:
			a.append(0.0)
print('The array is \n',array(a).reshape(r,c))  # reshape is use for create the array row and column wise
