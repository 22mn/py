gifdir = "./pics/"

from tkinter import *
win = Tk()
img = PhotoImage(file=gifdir+"one.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2,2,image=img, anchor=NW)
win.mainloop()