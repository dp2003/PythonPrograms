class Demo:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __del__(self):
		print("Object Destroyed")
d1=Demo(2,3)
d2=Demo(4,5)

del d1
del d2
'''print(Demo.__doc__)
print(Demo.__name__)
print(Demo.__dict__)
print(d1.__dict__)
print(Demo.__module__)
print(Demo.__bases__)'''