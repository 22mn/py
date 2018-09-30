from tkinter import *
from tkinter102 import MyGui

# main app window
mainwin = Tk()
Label(mainwin, text = __name__).pack()
#MyGui(mainwin).pack(side=RIGHT)

# pop up window
popup = Toplevel()
Label(popup, text = "Attach").pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()