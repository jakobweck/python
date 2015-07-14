from Tkinter import *
from ConfigParser import *
import pygame, sys
import importlib
class introWindow:
	def __init__(self, master):
		introFrame = Frame(master)
		introFrame.pack()
		self.introtext = Label(
			introFrame, text="WELCOME TO GAME")
		self.introtext.grid(row=0, columnspan=2)
		self.newgame = Button(
			introFrame, text="NEW GAME", command=introFrame.quit)
		self.newgame.grid(row=1, column=0)
		
		self.loadgame = Button(
			introFrame, text="LOAD SAVE", command=self.loadsave)
		self.loadgame.grid(row=1, column=1)
	def loadsave(self):
		lswindow = Toplevel()
		lswindow.wm_title("Load Save")
		self.lstext = Label(
			lswindow, text="Enter the filename of your save")
		self.lstext.grid(row=0)
		self.saveentry = Entry(lswindow)
		self.saveentry.grid(row=1)
		self.load = Button(
			lswindow, text="LOAD SAVE", command=self.submitsave)
		self.load.grid(row=2) 
	def submitsave(self):
		savename=self.saveentry.get()
		savefile = importlib.import_module("package.path.%s" % savename)
root = Tk()

app = introWindow(root)
root.mainloop()
