try:
	fieptr=open("file1.txt","r")
	a= 5/0
	
except ArithmeticError:
	print("Divisor by zero")
except IOError:
	print("File not found")
else:
	print("End Program")