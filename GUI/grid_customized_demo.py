from tkinter import *
def add():
    num1=float(e1.get())
    num2=float(e2.get())
    ans=num1+num2
    rst_e.insert(0,str(ans))
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    rst_e.delete(0,END)
master = Tk()
# this wil create a label widget
l1 = Label(master, text = "First:")
l2 = Label(master, text = "Second:")
# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = S, pady = 2,ipadx=20)
l2.grid(row = 1, column = 0, sticky = S, pady = 2,ipady=20)
# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)
# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
rst_lbl = Label(master,text="Result:")
rst_lbl.grid(row = 2, column = 0, pady = 2)
rst_e = Entry(master)
rst_e.grid(row = 2, column = 1, pady = 2)
add_btn = Button(master,text="Add", command=add)
clr_btn = Button(master,text="Clear", command=clear)
add_btn.grid(row = 3, column = 0, pady = 2)
clr_btn.grid(row = 3, column = 1, pady = 2)
mainloop()