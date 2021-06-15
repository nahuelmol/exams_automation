from tkinter import *


def create_window(window):
	print("there's a window")

	lbl=Label(window, text="This is Label widget", fg='black', font=("Helvetica", 16))
	lbl.place(x=60, y=50)

	btn = Button(window, text="View exams", fg='black')
	btn.place(x=80, y=100)

	########################################################
	btn = Button(window, text="Make a new exam", fg='black')
	btn.place(x=300, y=160)

	btn = Button(window, text="Edit an exam", fg='black')
	btn.place(x=300, y=130)

	btn = Button(window, text="Delete an exam", fg='black')
	btn.place(x=300, y=100)

	btn = Button(window, text="With 1 themes", fg='black')
	btn.place(x=450, y=160)

	btn = Button(window, text="Multiple themes", fg='black')
	btn.place(x=450, y=190)

	########################################################
	window.title("New window") 
	window.geometry("600x400+10+20")
	window.mainloop()

if __name__ == 'interface.index':

	window = Tk()
	create_window(window)

