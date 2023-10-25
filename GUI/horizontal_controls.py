from tkinter import *
# from tkinter.ttk import *
w = Tk() 
# cretaing a Frame which can expand according
# to the size of the window
f = Frame(w)
f.pack(fill = BOTH, expand = True)
# button widgets which can also expand and fill
# in the parent widget entirely
b1 = Button(f, text = "Button1!!!",
            background = "red", fg = "white")
b1.pack(side = LEFT, expand = True, fill = BOTH)
b2 = Button(f, text = "Button2!!!",
            background = "blue", fg = "white")
b2.pack(side = RIGHT, expand = True, fill = BOTH)
b3 = Button(f, text = "Button3!!!",
            background = "green", fg = "white")
b3.pack(side = LEFT, expand = True, fill = BOTH)
w.mainloop()