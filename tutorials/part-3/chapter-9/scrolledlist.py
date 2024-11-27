""" a simple customizable scrolled listbox component"""

from tkinter import *
class ScrolledList(Frame):
 	def __init__(self, options, parent=None):
 		Frame.__init__(self, parent)
 		self.pack(expand=YES, fill=BOTH)
 		self.makeWidgets(options)

 	def handleList(self, event):
 		index = self.listbox.curselection()
 		label = self.listbox.get(index)
 		self.runCommand(label)

 	def makeWidgets(self, options):
 		sbar = Scrollbar(self)
 		lst = Listbox(self, relief=SUNKEN)
 		sbar.config(command=lst.yview)
 		lst.config(yscrollcommand=sbar.set)
 		sbar.pack(side=RIGHT, fill=Y)
 		lst.pack(side=LEFT, expand=YES, fill=BOTH)
 		pos = 0
 		for label in options:
 			lst.insert(pos, label)
 			pos += 1
 		#lst.config(selectmode=SINGLE,setgrid=1)
 		lst.bind("<Double-1>", self.handleList)
 		self.listbox = lst

 	def runCommand(self, selection):
 		print("You selected: ", selection)

if __name__ == '__main__':
 	options = (("Lumberjack-%s" %s) for s in range(20))
 	ScrolledList(options).mainloop()