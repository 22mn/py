from tkinter import *

root = Tk()
lab = Label(root)
ent = Entry(root)
var = StringVar()
ent.config(textvariable=var)
lab.pack(side=TOP)
ent.pack(side=TOP, fill=X)

def change(event):
	lab.config(text=ent.get())

ent.bind("<KeyRelease>", change)
root.mainloop()