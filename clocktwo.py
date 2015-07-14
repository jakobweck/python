from Tkinter import *
import time 
#main class
class Clock:
	def __init__(self, master, hr, min, sec):
		self.h = StringVar()
		self.m = StringVar()
		self.s = StringVar()
		self.h.set(hr)
		self.m.set(min)
		self.s.set(sec)
		#create frame for all labels
		main = Frame(master)
		main.pack()
		#pass time args to variables?? should
		#label for hour (top left)
		self.hour = Label(
			main, textvariable = self.h
			)
		self.hour.grid(row=0, column=0)
		#label for minute (top middle)
		self.minute = Label(
			main, textvariable=self.m
			)
		self.minute.grid(row=0, column=1)
		#label for second (top right)
		self.second = Label(
			main, textvariable=self.s
			)
		self.second.grid(row=0, column = 2)
		#quit button (bottom)
		self.exit = Button(
			main, text = "QUIT", command=main.quit
			)
		self.exit.grid(row=1, column=1)
		self.master = master
		self.poll()
	def poll(self):
		self.h.set(time.strftime("%I"))
		self.m.set(time.strftime("%M"))
		self.s.set(time.strftime("%S"))
		self.master.after(1000, self.poll)
#create window			
root = Tk()
#call class in window
app = Clock(root,time.strftime("%I"),time.strftime("%M"),time.strftime("%S"))
#begin
root.mainloop()
root.update()
