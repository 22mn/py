from menu_frm import makemenu
from tkinter import *

root = Tk()
for i in range(3):
	frm = Frame(root)
	menu = makemenu(frm)
	menu.config(bd=2, relief=RAISED)
	frm.pack(expand=YES, fill=BOTH)
	Label(frm, bg="black", height=5, width=25).pack(expand=25, fill=BOTH)
Button(root, text="Bye", command= root.destroy).pack()
root.mainloop()