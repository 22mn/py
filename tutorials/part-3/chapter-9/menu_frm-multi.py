from menu_frm import makemenu
from tkinter import *

root = Tk()
for i in range(2):
	menu = makemenu(root)
	menu.config(bd=2, relief=RAISED)
	Label(root, bg="black", height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text="Bye", command=root.destroy).pack()
root.mainloop()