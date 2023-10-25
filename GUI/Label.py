from tkinter import *
window = Tk()
window.title("Label Demo ")
label = Label(window, text="Label").pack()
button=Button(window, text="Button")
button.pack()
txt = Entry(window,text="Textfield")
txt.pack()
window.mainloop()