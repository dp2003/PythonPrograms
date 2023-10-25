from tkinter import *
  
root = Tk()
root.geometry("500x500")
root.title("Revovery Rate")
  
def Take_input():
    name = inputtxt2.get("1.0", "end-1c")
    affected_int = int(affected.strip())
    recovered = inputtxt4.get("1.0", "end-1c")
    recovered_int = int(recovered.strip())
    Output.insert(END, str((recovered_int / affected_int) * 100) + "%")
      
l1 = Label(text = "Name")
l1.pack()
inputtxt1 = Text(root, height = 1, width = 25)
inputtxt1.pack()

l2 = Label(text = "Affected")
l2.pack()
inputtxt2 = Text(root, height = 1,width = 25)
inputtxt2.pack()

l3 = Label(text = "Deaths")
l3.pack()
inputtxt3 = Text(root, height = 1,width = 25)
inputtxt3.pack()

l4 = Label(text = "Recovered")
l4.pack()
inputtxt4 = Text(root, height = 1,width = 25)
inputtxt4.pack()

Display = Button(root, height = 2,width = 20, text ="CalRecovery",command = lambda:Take_input())
Display.pack()
Output = Text(root, height = 5, width = 25)
Output.pack()  
mainloop()
