from tkinter import *

root = Tk()
a = StringVar()
ent = Entry(root)
Label(root,textvariable=a).pack()
def digit(_type, _digit,_length, idx):
	#ent.icursor(0)
	print("Type : ", _type)
	print("Digit :",_digit)
	print("Length :",_length)
	
	if _type == "1":
		if _digit.isdigit() and len(_length)==1:
			a.set(_length)
			#ent.config(state=DISABLED)
			return True
		else:
			return False
	if _type == "0":
		return True

def callme(event):
	ent.config(state=NORMAL)
	ent.delete(0,END)

reg = root.register(digit)
ent.config(validate="key", validatecommand=(reg,"%d","%S","%P", "%i"))
ent.bind("<FocusIn>",callme)
Entry(root).pack()
ent.pack()

root.mainloop()