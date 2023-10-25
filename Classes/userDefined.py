class SalaryNotInRangeError(Exception):

	def __init__(self,salary,message="Salaray is not in range(5000-10000)"):
		self.salary=salary
		self.message=message
		#super().__init__(self.message)


salary=int(input("Enter salary amount:"))
if not 5000<salary<10000:
	raise SalaryNotInRangeError(salary)