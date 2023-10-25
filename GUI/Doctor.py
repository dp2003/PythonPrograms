import mysql.connector
from tkinter import * 
root = Tk()
root.geometry("500x500")
root.title("Doctors")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

if mydb:
  print("Connection Established Successfully")
else:
  print("Connection Error")
  
def Take_input():
    id= inputtxt1.get()
    name = inputtxt2.get()
    special = inputtxt3.get()
    exp = inputtxt4.get()   
 
l1 = Label(text = "ID")
l1.pack()
inputtxt1 = Text(root, height = 1, width = 25)
inputtxt1.pack()

l2 = Label(text = "Name")
l2.pack()
inputtxt2 = Text(root, height = 1,width = 25)
inputtxt2.pack()

l3 = Label(text = "Specialization")
l3.pack()
inputtxt3 = Text(root, height = 1,width = 25)
inputtxt3.pack()

l4 = Label(text = "Experience")
l4.pack()
inputtxt4 = Text(root, height = 1,width = 25)
inputtxt4.pack()

l4 = Label(text = "Hospital Name:")
l4.pack()
inputtxt4 = Text(root, height = 1,width = 25)
inputtxt4.pack()

Display = Button(root, height = 2,width = 20, text ="Add Doctor",command = lambda:Take_input())
Display.pack()

mainloop()
