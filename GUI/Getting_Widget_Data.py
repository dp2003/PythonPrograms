from tkinter import * 
from tkinter.ttk import *
window = Tk()
window.geometry("400x300")
window.title("Label Demo")
label = Label(window, text ="LABEL1")
bttn1 = Button(window, text = "BUTTON1")
bttn1.pack()
txt1 = Entry(window, text = "ENTRY1")
#Setting Default Text of Entry Widget
txt1.insert(0, "This is the default text")
# OR
"""
text = StringVar()
text.set("This is the default text")
textBox = Entry(window,textvariable = text)
textBox.pack()
"""
txt1.pack()
#Getting label text
print(label.cget("text"))
print(label["text"])
# Setting Button text
bttn1["text"]="Text Set"
label.pack(); #pack() method is to be invoked at the last
#Getting entry text
print("Entry Text=",txt1.get())
def handle_click(event):
	print("The button was clicked ")
button=Button(window,text="Click me!").pack()
window.bind("<Button-1>",handle_click)
window.mainloop()