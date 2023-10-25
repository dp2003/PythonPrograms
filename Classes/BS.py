class BookStore:
  TBooks=0
  def __init__(self,t,a,qty,price):
      print("Welcome to the constructor")
      self.title=t
      self.author=a
      self.qty=qty
      self.price=price
      BookStore.TBooks+=1
  def getBook(self):
        print("Title=",self.title)
        print("Author=",self.author)
        print("Quantity=",self.qty)
        print("Price=",self.price)
#(instance)object creation
B1=BookStore("Python Programming","Andrew NG",20,350)
print("Total Books=",BookStore.TBooks)
B2=BookStore("ANSI C","E Balagurusamy",50,300)
print("Total Books=",BookStore.TBooks)
print("\nBook Details:")
B1.getBook()
print("\nBook Details:")
B2.getBook()
#Array of objects
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