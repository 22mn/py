from tkinter import *

rows, columns = 9,9

root = Tk()
frame = Frame(root, bg="beige", relief=RAISED, bd=2)
frame.grid()

# store value/StringVar() for each cell 
ValueDict = {}
for i in range(81):
	ValueDict[str(i)] = StringVar()

# trace callback 
def hola(*args):
	# args[0] StringVar()
	cellnum = args[0][6:]
	# input value
	value = ValueDict[str(cellnum)].get()
	
	# check digit
	if value.isdigit() and value != "0":
		# allow only one digit 
		ValueDict[str(cellnum)].set(value[:1])
		value = ValueDict[str(cellnum)].get()

		# cursor blink offtime after input
		allentries[int(cellnum)].config(insertofftime=100000)
		print(" cell no: ", cellnum )
		print(" input value: ", value)
	else:
		ValueDict[str(cellnum)].set("")
		print("Must be digit!")
count = 0

allentries = []

for row in range(rows):
	for column in range(columns):
		ent = Entry(frame, width=3, relief=SUNKEN,fg="green",
				textvariable=ValueDict[str(count)])
		# font
		ent.config(font=("Calibri", 28, "bold"))
		# text center
		ent.config(justify = CENTER)
		# cursor size and blink time
		ent.config(insertontime=700, insertwidth="0.2mm")

		ent.grid(row=row,column=column,sticky=NSEW)
		ValueDict[str(count)].trace("w", hola)    # "write" mode trace callback
		allentries.append(ent)
		count +=1
#allentries = frame.winfo_children()
root.mainloop()
