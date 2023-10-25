#import tkinter as tk
from tkinter import * 
window = Tk()

for i in range(3):
    for j in range(3):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()