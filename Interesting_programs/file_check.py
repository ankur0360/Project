try:    
	a = open('hi.txt','r')    # try open hi.txt file
except IOError:             # it raised when an input/output operation fails
	print('The file does not exits')    
else:    
	print('The file is exists')    
a.close()                   # cosing the file
