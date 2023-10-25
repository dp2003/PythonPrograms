print("Enter the values of Side1,Side2 and Side3")
x=int(input())
y=int(input())
z=int(input())

if x==y and y==z:
	print("Equilateral Triangle")
elif x==y or y==z or x==z:
	print("Scalene Triangle")
else:
	print("Isosceles Triangle")

