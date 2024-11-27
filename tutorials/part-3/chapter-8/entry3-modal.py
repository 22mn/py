# can fetch values after destroy with stringvars

from tkinter import *
from entry3 import makeform, fetch, fields

def show(variables, popup):
	fetch(variables)
	popup.destroy()

def ask():
	popup = Toplevel()
	vars = makeform(popup, fields)
	Button(popup, text="OK", command=(lambda: show(vars, popup))).pack()
	popup.grab_set()
	popup.focus_set()
	popup.wait_window()

root = Tk()
Button(root, text="Dialog", command=ask).pack()
root.mainloop()