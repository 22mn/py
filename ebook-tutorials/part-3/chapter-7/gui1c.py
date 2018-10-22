from tkinter import *

def quit(name):
	print("%s quit!" %name)
	root.destroy()

root = Tk()
root.title("Hola")
widget = Button(root, text="Hello GUI world", command=(lambda : quit("mgj")))
# use lambda to prevent invocation on button construction "command= quit('mgj')"
# another way (lambda: print("mgj quit!") or root.destroy())
widget.pack(side=TOP, expand=YES, fill=X)
root.mainloop()