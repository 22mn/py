"""
image viewer extension: uses fixed-size thumbnail buttons for uniform layout, and
adds scrolling for large sets by displaying thumbs in a canvas widget with
scroll bars; requires PIL to view image formats such as JPEG, and reuses thumbs
maker and single photo viewer in viewer_thumbs.py; caveat/to do: this could also 
scroll popped-up images that are too large for the screen, and are cropped on
Windows as is; see PyPhoto later in Chapter 11 for a much more complete version;
"""

import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne

def viewer(imgdir, kind=Toplevel, numcols=None, height=300, width=300):
	"""
	use fixed-size buttons, scrollable canvas;
	sets scrollable (full) size, and places thumbs at absolute x,y
	coordinates in canvas; caveat: assumes all thumbs are same size
	"""

	win = kind()
	win.title("Simple viewer: " + imgdir )
	quit = Button(win, text="Quit", command=win.quit, bg="beige")
	quit.pack(side=Button, fill=X)

	canvas = Canvas(win, borderwidth=0)
	vbar = Scrollbar(win)
	hbar = Scrollbar(win, orient="horizontal")

	vbar.pack(side=RIGHT, fill=Y)
