from Tkinter import *
class TTT:

	def __init__(self,master):
		#create window
		global button_name 
		main = Frame(master)
		main.pack()
		#array of names for ttt boxes
		boxes = ["one", "two"]
		#initialize column and row variables to generate boxes
		colvar = -1
		rowvar = 0
		#generate 9 boxes without repeating yourself
		for i in boxes:
		#for every entry in the box list, create a button with that entry as its text
			self.i = Button(main,text = "%s" % i, command = self.changetext())
			button_name = "%s" % i 
			#increment the column the button will be placed in by one BEFORE placing it
			colvar += 1
			#place the button
			self.i.grid(column = colvar, row = rowvar)
			#if the button is in the far right column, increment the row that the next button will be in and reset the column to far left
			if colvar == 2:
				rowvar +=1
				colvar = -1
			#if the button is in another column, do nothing
			else:
				pass
	def changetext(self):
		  print button_name
root = Tk()
app = TTT(root)

root.mainloop()