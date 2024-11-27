from tkinter import *

def greeting():
	print("Hello stdout world!...")

win=Frame()

win.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text="Hello", command=greeting).pack(side=LEFT,anchor=N,fill=Y)
Label(win, text="Hello container world").pack(side=TOP)
Button(win, text="Quit", command=win.quit).pack(side=RIGHT,fill=X,expand=YES)

win.mainloop()