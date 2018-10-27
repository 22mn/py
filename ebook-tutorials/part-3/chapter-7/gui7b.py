from tkinter import *
from gui7 import HelloPackage

frm = Frame()
frm.pack()
Label(frm, text="Hello").pack()

part = HelloPackage(frm)
part.top.pack(side=RIGHT)
frm.mainloop()