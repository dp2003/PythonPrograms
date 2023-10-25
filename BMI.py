print("Enter your height in meter :")
height=float(input())
print("Enter your weight in kg :")
weight=float(input())
BMI= weight/(height*height)
print("BMI =",BMI)

if  BMI < 18.5:
   print("underweight")

elif BMI >= 18.5 and BMI <=24.9:
   print("Normal weight")

elif BMI >= 25 and BMI <= 29.9:
   print("Overweight")

else:
	print("Obesity")