from Tkinter import *
import time 
#main class
class Clock:
	def __init__(self, master):
		#init variables containing times pulled from system
		self.h = StringVar()
		self.m = StringVar()
		self.s = StringVar()
		self.ampm = StringVar()
		self.h.set(time.strftime("%I"))
		self.m.set(time.strftime("%M"))
		self.s.set(time.strftime("%S"))
		self.ampm.set(time.strftime("%p"))
		#create frame for all labels
		main = Frame(master)
		main.pack()
		#label for hour (top left)
		self.hour = Label(
			main, textvariable = self.h, font =("Helvetica", 16)
			)
		self.hour.grid(row=0, column=0)
		#colon between hour and minute
		Label(main, text=":").grid(row=0, column=1)
		#label for minute (top middle)
		self.minute = Label(
			main, textvariable=self.m, font =("Helvetica", 16)
			)
		self.minute.grid(row=0, column=2)
		#Colon between minute and second
		Label(main, text=":").grid(row=0, column=3)
		#label for second (top right)
		self.second = Label(
			main, textvariable=self.s, font =("Helvetica", 16)
			)
		self.second.grid(row=0, column = 4)
		#AM or PM (top far right)
		self.meridian = Label(
			main, textvariable=self.ampm, font=("Helvetica", 16)
			)
		self.meridian.grid(row=0, column = 5)
		#quit button (bottom)
		self.exit = Button(
			main, text = "QUIT", command=main.quit, padx=20
			)
		self.exit.grid(row=0, column=6)
		#run update function
		self.master = master
		self.poll()
	#every second (1000 ms), update times from system and repeat
	def poll(self):
		self.h.set(time.strftime("%I"))
		self.m.set(time.strftime("%M"))
		self.s.set(time.strftime("%S"))
		self.ampm.set(time.strftime("%p"))
		self.master.after(1000, self.poll)
#create window			
root = Tk()
#custom favicon and title
root.iconbitmap(bitmap="D:\Documents\untitled.ico")
root.wm_title("System Clock")
#window size in pixels locked to 225x30
root.maxsize(width = 225, height = 30)
root.minsize(width = 225, height = 30)
#call class in window
app = Clock(root)
#begin
root.mainloop()

