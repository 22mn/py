

#***NOTE*** 
#(ENTRY IS NOT USING ANYMORE) 
#(DRAG AND DROP MAY BE)
from tkinter import *

rows, columns = 9,9

root = Tk()
frame = Frame(root, bg="beige", relief=RAISED, bd=2)
frame.grid()

# store value/StringVar() for each cell 
ValueDict = {}
for i in range(81):
	ValueDict[str(i)] = StringVar()

userSteps = {}
memory = []
toUndo = []
toRedo = []

# trace callback 
def hola(*args):
	global memory
	# args[0] StringVar()
	cellnum = args[0][6:]
	# input value
	value = ValueDict[str(cellnum)].get()
	
	# check digit
	if value.isdigit() and value != "0":
		# allow only one digit 
		ValueDict[str(cellnum)].set(value[:1])
		# cursor blink offtime after input
		allentries[int(cellnum)].config(insertofftime=100000)

		# process to trace user steps
		memory.append(cellnum)
		toUndo.append(cellnum)
		userSteps[cellnum] = value

		print(" cell no: ", cellnum )
		print(" input value: ", value)
count = 0

allentries = []


def hello(args):
	print("hello function")
	print(args.widget.get())
	print(args.char)


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

		#***Test Validate***
		# callback one time only (not using)
		#ent.config(validate="focus", validatecommand=lambda ent=ent: hello(ent))

		# ***Bind***
		# call everytime focus-in (considering)
		ent.bind("<FocusIn>",hello)

		ent.grid(row=row,column=column,sticky=NSEW)
		
		# "write" mode trace callback
		ValueDict[str(count)].trace("w", hola)

		allentries.append(ent)
		count +=1
#allentries = frame.winfo_children()

def undo():
	global toUndo,toRedo, memory
	if toUndo:
		toRedo = memory[len(toUndo)-1 : len(memory)]
		currentEntry = toUndo[-1]
		toUndo = toUndo[:-1]
		ValueDict[currentEntry].set("")
	else:
		print("Not input yet!")

undoButton = Button(frame, text="Undo", command=undo)
undoButton.grid(row=rows+1 , column=1, sticky=NSEW,columnspan=2, pady=5)


def redo():
	global toRedo,toUndo,memory
	if toRedo:
		currentEntry = toRedo[0]
		toRedo = toRedo[1:]
		ValueDict[currentEntry].set(userSteps[currentEntry])
	else:
		print("Here is your last moved!")
		

redoButton = Button(frame, text="Redo", command=redo)
redoButton.grid(row=rows+1, column=6, sticky=NSEW, columnspan=2, pady=5)

root.mainloop()
