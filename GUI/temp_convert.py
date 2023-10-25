from tkinter import *
def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = txt_temp.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
window = Tk()
window.title("Temperature Converter")
frm_entry = Frame(master=window)
txt_temp = Entry(master=frm_entry, width=10)
lbl_temp = Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
txt_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
#txt_temp.pack()
#lbl_temp.pack()
btn_convert = Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
#frm_entry.pack()
window.mainloop()