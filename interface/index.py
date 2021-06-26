from tkinter import *
from .button import *

def create_window(window):
	print("there's a window")

	lbl=Label(window, text="This is Label widget", fg='black', font=("Helvetica", 16))
	lbl.place(x=60, y=50)

	btn = Button(window, text="View exams", fg='black')
	btn.place(x=80, y=100)

	txtfld=Entry(window, text="This is Entry Widget", bd=5)
	txtfld.place(x=80, y=150)

	window.title("New window") 
	window.geometry("600x400+10+20")
	window.mainloop()

if __name__ == 'interface.index':

	window = Tk()
	create_window(window)

