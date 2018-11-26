"""
Tk 8.0 style main window menus
menu/tool bars packed before middle, fill=X (pack first=clip last);
add photo menu entries; see also: add_checkbutton, add_radiobutton
"""

from tkinter import *
from tkinter.messagebox import *


class NewMenuDemo(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.createWidgets()
		self.master.title("Toolbars and Menus")
		self.master.iconname("tkpython")

	def createWidgets(self):
		self.makeMenuBar()
		self.makeToolBar()
		L = Label(self, text="Menu and Toolbar Demo")
		L.config(relief=SUNKEN, width=40, height=10, bg="white")
		L.pack(expand=YES, fill=BOTH)

	def makeToolBar(self, size=(40,40)):

		toolbar = Frame(self, cursor="hand2", relief=SUNKEN, bd=2)
		toolbar.pack(side=BOTTOM, fill=X)
		imgdir = "../chapter-8/pics/"
		photos = ("one.gif","two.gif","three.gif")
		self.toolPhotoObjs=[]
		for file in photos:
			img = PhotoImage(file= imgdir + file)
			btn = Button(toolbar, image=img, command=self.greeting)
			btn.config(relief=RIDGE, bd=5)
			btn.config(width=size[0], height=size[1])
			btn.pack(side=LEFT)
			self.toolPhotoObjs.append(img)
		Button(toolbar, text="Quit", command=self.quit).pack(side=RIGHT, fill=Y)

	def makeMenuBar(self):
		self.menubar = Menu(self.master)
		self.master.config(menu=self.menubar)
		self.fileMenu()
		self.editMenu()
		self.imageMenu()

	def fileMenu(self):
		pulldown = Menu(self.menubar)
		pulldown.add_command(label="Open...", command=self.notdone)
		pulldown.add_command(label="Quit", command=self.destroy)
		self.menubar.add_cascade(label="File", menu=pulldown, underline=0)

	def editMenu(self):
		pulldown = Menu(self.menubar)
		pulldown.add_command(label="Paste", command=self.notdone)
		pulldown.add_command(label="Spam", command=self.greeting)
		pulldown.add_separator()
		pulldown.add_command(label="Delete",command=self.greeting)
		pulldown.entryconfig(4, state=DISABLED)
		self.menubar.add_cascade(label="Edit", underline=0, menu=pulldown)

	def imageMenu(self):
		photoFiles = ("one.gif","two.gif","three.gif")
		pulldown = Menu(self.menubar)
		self.photoObjs =[]
		for file in photoFiles:
			img = PhotoImage(file="../chapter-8/pics/" + file)
			pulldown.add_command(image=img, command=self.notdone)
			self.photoObjs.append(img)
		self.menubar.add_cascade(label="Image", underline=0, menu=pulldown)

	def greeting(self):
		showinfo("greeting", "Greeting")

	def notdone(self):
		showerror("Notimplemented", "Not yet available")

	def quit(self):
		if askyesno("Verify quit", "Are you sure you want to quit?"):
			Frame.quit(self)

if __name__ == '__main__':
	NewMenuDemo().mainloop()


