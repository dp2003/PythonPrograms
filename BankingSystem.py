class BankingSystem:

	def __init__(self,acc_no,pin):
		self.acc_no=acc_no
		self.pin=pin

class BankingFunctions(BankingSystem):
	def __init__(self,):
		super().__init__(acc_no,pin)
		self.balance=0
		print("WELCOME TO THE BANK ")

	def deposit(self):
		print("\n_______________Deposit Amount_______________\n")
		print("Enter amount you want to deposit: ")
		amt=float(input())
		self.balance += amt
		print("Rs.",amt," Deposited!!")

	def withdraw(self):
		print("\n_______________Withdraw Amount_______________\n")
		print("Enter amount to be Withdrawan: ")
		amt=float(input())

		if self.balance>=amt:
			self.balance-=amt
			print("Rs.",amt,"Withdrawan!!")
		else:
			print("Your account balance is insufficient!!")

	def display_bal(self):
		print("\n_______________Balance_______________\n")
		print("Net Balance: ",self.balance)

print("\n_______________Banking Management System______________\n")
print("Enter Account No. and pin.")
acc_no=int(input())
pin=int(input())
bs=BankingSystem(acc_no,pin)
if acc_no==401 and 	pin==202:
	print("Logged in Succesfully!!")		
	bf=BankingFunctions()
	bf.deposit()
	bf.withdraw()
	bf.display_bal()
else:
	print("Login not Succesfull!! Please try again..")
