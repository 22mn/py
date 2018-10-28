import tkinter
from tkinter import Tk, Button
tkinter.NoDefaultRoot()

win1 = Tk()
win2 = Tk()

Button(win1, text="spam", command=win1.destroy).pack()
Button(win2, text="spam", command=win1.destroy).pack()

win1.mainloop()