class Vaccine:
	def __init__(self,vid,company,effect,price,country):
		self.__vid=vid
		self.__company=company
		self.__effect=effect
		self.__price=price
		self.__country=country
	def addVaccine(self):
		print("Enter Vaccine id,Company name, effectiveness, price(per dose) and country:")
		vid=int(input())
		company=input()
		effect=int(input())
		price=float(input())
		country=input()
	def displayVaccine(self):
		print("Vacccine id:",vid)
		print("Company Name:",company)
		print("Effectiveness:",effect)
		print("Price:",price)
		print("Country:",country)
	def maxEffectiveVaccine(self):
		if self.effect==85:
			print("85%/ effective")
		elif self.effect==95:
			print("95%/ ie maximum effectiveness")

vac=Vaccine()
vac.addVaccine()
vac.displayVaccine()
vac.maxEffectiveVaccine()
