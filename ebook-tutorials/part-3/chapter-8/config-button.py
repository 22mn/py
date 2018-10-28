from tkinter import *

widget=Button(text="spam", padx=10,pady=10)
widget.pack(padx=5,pady=5)
widget.config(cursor="gumby")
widget.config(bd=8,relief=RAISED)
widget.config(bg="dark green", fg="white")
widget.config(font=("helvatica", 20, "underline italic"))
mainloop()