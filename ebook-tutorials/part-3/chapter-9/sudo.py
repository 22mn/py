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
	print("hola amigo")
	# args[0] StringVar()
	print(args[0][6:])

count = 0

for row in range(rows):
	for column in range(columns):
		ent = Entry(frame, width=3, relief=SUNKEN,fg="green",
				textvariable=ValueDict[str(count)])
		ent.grid(row=row,column=column)
		ValueDict[str(count)].trace("w", hola)    # "write" mode trace callback
		count +=1

root.mainloop()
