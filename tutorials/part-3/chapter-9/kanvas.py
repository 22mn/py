# drawing board 

from tkinter import *

root = Tk()
canvas = Canvas(root,height=500, width=500, bg="beige")
canvas.pack()

startX, startY = 0,0

def on_start(event):
	global startX, startY
	startX , startY = event.x, event.y

def drag_end(event):
	global startX, startY
	#print("Start (%s, %s)" %(startX, startY))
	#print("Event (%s, %s)" %(event.x, event.y))
	canvas.create_line(startX, startY, event.x,event.y)
	startX, startY = event.x, event.y

def clear(event):
	event.widget.delete("all")


canvas.bind("<ButtonPress-1>", on_start)
canvas.bind("<B1-Motion>", drag_end)
canvas.bind("<ButtonPress-3>", clear)

canvas.mainloop()