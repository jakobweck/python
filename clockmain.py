from Tkinter import *
import time
h = StringVar()
h.set(time.strftime("%I"))
m = StringVar()
m.set(time.strftime("%M"))
s = StringVar()
s.set(time.strftime("%S"))
#main class
class Clock:
	def __init__(self, master, hour, minute, second):
		#create frame for all labels
		main = Frame(master)
		main.pack()
		#init variables for time components
		self.hour = h 
		self.minute = m
		self.second = s
		#label for hour (top left)
		self.hour = Label(
			main, textvariable=self.hour
			)
		self.hour.grid(row=0, column=0)
		#label for minute (top middle)
		self.minute = Label(
			main, textvariable=self.minute
			)
		self.minute.grid(row=0, column=1)
		#label for second (top right)
		self.second = Label(
			main, textvariable=self.second
			)
		self.second.grid(row=0, column = 2)
		#quit button (bottom)
		self.exit = Button(
			main, text = "QUIT", command=main.quit
			)
		self.exit.grid(row=1, column=1)

			
#create window			
root = Tk()
#call class in window
app = Clock(root)
#begin
root.mainloop()