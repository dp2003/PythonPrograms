# Importing tkinter module
from tkinter import * 
from tkinter.ttk import *
 
# creating Tk window
master = Tk()
 
# cretaing a Frame which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)
 
# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Button1")
#b1.pack()
b1.pack(fill = X, expand = True)
 
# Button 2
b2 = Button(pane, text = "Button2")
#b2.pack()
b2.pack(fill = Y, expand = True)
 
# Execute Tkinter
master.mainloop()