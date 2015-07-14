from Tkinter import *
import tkMessageBox
import datetime
class SecondsFinder:
	def __init__(self, master):
		main = Frame(master)
		main.pack()
		yearfield = Entry(main)
		yearfield.grid(row = 0, column = 0)
		yearfield.insert(0, "Year of Birth")
		monthfield = Entry(main)
		monthfield.grid(row = 1, column = 0)
		monthfield.insert(0, "Month of Birth")
		dayfield = Entry(main)
		dayfield.grid(row = 2, column = 0)
		dayfield.insert(0, "Day of Birth")
		def callback():
			birthday = datetime.date(int(yearfield.get()), int(monthfield.get()), int(dayfield.get()))
			today = datetime.date.today()
			diff = today - birthday
			tkMessageBox.showwarning("asdf", diff.total_seconds())
		def fadeyear(event):
			ycurrent = yearfield.get()
			if ycurrent == "Year of Birth":
				yearfield.delete(0,END)
			elif ycurrent == "":
				yearfield.insert(0, "Year of Birth")
		yearfield.bind("<FocusIn>", fadeyear)
		yearfield.bind("<FocusOut>", fadeyear)
		submit = Button(main, text = "Submit", command = callback)
		submit.grid(row = 3, column = 0)

root = Tk()
app = SecondsFinder(root)
root.mainloop()