import threading
from threading import*
class myThread(Thread):
	def __init__(self,s,e):
		Thread.__init__(self):
		self.s=s
		self.e=e
		self.count=0

	def run(self):
		for i in range(self.s,self.e+1):
			if(i%7==0):
				print(current_thread.getname(),i)
				self.count+=1
				print("Count in each thread :",self.count)
t1=mythread(1,250)
t2=mythread(251,500)
t1.start()
t2.start()
t1.join()
t2.join()

