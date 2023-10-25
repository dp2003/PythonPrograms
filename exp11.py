import threading
from threading import*
counter=0
class myThread(Thread):
	def __init__(self,s,e):
		Thread._init_(self)
		self.s=s
		self.e=e
	def run(self):
		for i in range(self.s,self.e+1):
			if(i%7==0):
				print(i)
t1=myThread(1,100)
t2=myThread(101,200)
t3=myThread(201,300)
t4=myThread(301,400)
t5=myThread(401,500)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print(current_thread().getName())