class BookStore:
	TotalBooks=0
	def __init__(self,title,author,qty,price):
		print("Welcome to Constructor")
		self.title=title
		self.author=author
		self.qty=qty
		self.price=price
		BookStore.TotalBooks+=1

B1= BookStore("Python Programming","Andrew NG",20,250)
print("TotalBooks=",BookStore.TotalBooks)
B2= BookStore("ANSI C ","E Balagurusamy",50,300)
print("TotalBooks=",BookStore.TotalBooks)