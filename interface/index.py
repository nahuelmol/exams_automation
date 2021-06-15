from tkinter import *


def create_window(window):
	print("there's a window")

	btn = Button(window, text="First window", fg='blue')
	btn.place(x=80, y=100)

	window.title("New window") 
	window.geometry("300x200+10+20")
	window.mainloop()

if __name__ == 'interface.index':

	window = Tk()
	create_window(window)

