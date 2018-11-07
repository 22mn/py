from tkinter import *
root = Tk()
scale = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scale.pack(expand=YES, fill=Y)

def report():
	print(scale.get())

Button(root, text="state", command=report).pack(side=RIGHT)
root.mainloop()