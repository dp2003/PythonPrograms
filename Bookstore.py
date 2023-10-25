class BookStore:
	TotalBooks=0
	def _init_(self,title,author,qty,price):
		print("Welcome to _init_() constructor")
		title=title
		author=author
		qty=qty
		price=price
		BookStore.TotalBooks+=1
	def valuation(self):
		bookprice=Quantity*price
		print('bookprice=',bookprice)
	def getBook(self):
		print('Title=',title)
		print('Author=',author)
		print('Quantity=',qty)
		print('Price=',price)

'''b1=BookStore('python programming','balguruswami',20,30)
b2=BookStore("ANSI C","E Balagurusamy",50,300)
print("Total Book=",BookStore.TotalBooks)
print("\nBook details:")
b2.getBook()
print("\nBook valuation")
b2.valuation()'''

books=[]

print("How many books you want to enter?")

n=int(input())

for i in range(n):
	print("Enter title,author,quantity and price of book",i+1)
	title=input()
	author=input()
	qty=int(input())
	price=float(input())
	books.append(BookStore(title,author,qty,price))

# Displaying book details

#for i in range(len(books)):

#books[i].getBook()

for book in books:
	print(book)
	book.getBook()