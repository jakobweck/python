from Tkinter import *
import time 
#main class
class Clock:
	def __init__(self, master):
		#init variable to contain time
		self.time = StringVar()
		#Set variable to contain time and am/pm status pulled from system clock
		self.time.set(time.strftime("%I:%M:%S %p"))
		#create frame for all widgets
		main = Frame(master) 
		main.pack()
		#time display label
		self.t = Label( 
			main, textvariable = self.time, font =("Helvetica", 16)
			)
		self.t.grid(row=0, column=0)
		#quit button
		self.exit = Button(
			main, text = "QUIT", command=main.quit, padx=20
			)
		self.exit.grid(row=0, column=1)
		#run update function
		self.master = master
		self.poll()
	#every second (1000 ms), update time from system and repeat
	def poll(self):
		self.time.set(time.strftime("%I:%M:%S %p"))
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

