def legs(a,b): # defining function
	c = b / 2 - a
	d = a - c
	print('Total number of goats =',c,'\nTotal number of Chicken =',d)
print('Find the number of goats and Chicken')
x = int(input('Enter the number of Heads : '))
y = int(input('Enter the numbers of feets : '))
legs(x,y)     # funtion calling 
