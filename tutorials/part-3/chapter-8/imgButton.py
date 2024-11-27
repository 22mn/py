gifdir = "./pics/"

from tkinter import *

win = Tk()
img = PhotoImage(file=gifdir+"one.gif")
Button(win,image=img).pack()
win.mainloop()