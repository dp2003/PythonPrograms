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