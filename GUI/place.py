import tkinter as tk
window = tk.Tk()
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)
label2 = tk.Label(master=frame, text="I'm at (50, 50)", bg="yellow")
label2.place(x=50 ,y=50)
window.mainloop()