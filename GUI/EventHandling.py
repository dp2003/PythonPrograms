from tkinter import *
# Create a window object
window = Tk()
window.title("Key Event Window")
# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
    window.title("Key passed:" +event.char)
	# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

def handle_click(event):
	print("The button was clicked ")
button=Button(window,text="Click me!").pack()
window.bind("<Button-1>",handle_click)

window.mainloop()