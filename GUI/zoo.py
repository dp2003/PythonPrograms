from tkinter import *
import mysql.connector
from tkinter import messagebox
def _init_(self,window):
		self.window=window
		self.window.title("Animal zoo")
		self.window.geometry("2000x2000")

		frame=Frame(self.window,bg="black")
		frame.place(x=300,y=100,width=700,height=500)

		l2=Label(frame,text="Name :").place(x=20,y=10)
		l3=Label(frame,text="Age :").place(x=20,y=40)
		l4=Label(frame,text="Numbers:").place(x=20,y=60)
		l5=Label(frame,text="Country :").place(x=20,y=90)

		#en_id=Entry(window).place(x=70,y=10)
		self.en_name=Entry(frame).place(x=80,y=10)
		self.en_age=Entry(frame).place(x=80,y=40)
		self.en_number=Entry(frame).place(x=80,y=60)
		self.en_country=Entry(frame).place(x=80,y=90)

		add_btn=Button(frame,text="Add data",command=animaldata)
		add_btn.place(x=100,y=140)
def animaldata(self):	
	try:
		con=mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="animalzoo")
		cur=con.cursor()
		cur.execute("insert into details(name,age,number,country) values(%s,%s,%s,%s)",
					(self.en_name.get(),
					 self.en_age.get(),
					 self.en_number.get(),
					 self.en_country.get()
					))
		con.commit()
		con.close()
		messagebox.showinfo("Success","Inserted data successfully",parent=self.window)
	except Exception as es:
		messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.window)
 
#window=Tk()
#window.title("Animal zoo")
#l1=Label(window,text="ID :").place(x=20,y=10)
window=Tk()
obj=Animals()
window.mainloop()