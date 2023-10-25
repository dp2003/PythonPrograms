from tkinter import *
# Create a window object
window = Tk()
window.title("Key Event Window")
# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
# Run the event loop
window.mainloop()
