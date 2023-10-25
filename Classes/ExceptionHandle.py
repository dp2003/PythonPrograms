try:
	a= int(input("Enter a:"))
	b= int(input("Enter b:"))
	c=a/b
except Exception:
	print("Divisor can not be zero")
	print(Exception)
print("End Program")