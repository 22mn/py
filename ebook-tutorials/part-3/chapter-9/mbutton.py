from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack(side=TOP, fill=X)

mbutton = Menubutton(frame, text="Food")
picks = Menu(mbutton)

mbutton.config(menu=picks, bg='white')
mbutton.pack(side=LEFT)

picks.add_command(label="spam", command=root.destroy)
picks.add_command(label="eggs", command=root.destroy)
picks.add_command(label="bacon", command=root.destroy)

root.mainloop()