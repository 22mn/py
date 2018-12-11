# recode as an embeddable class
import sys
sys.path.append(r"../chapter-8")

from tkinter import *
from tkinter.filedialog import askopenfilename
from quitter import Quitter

class SumGrid(Frame):
	def __init__(self, parent=None, numrow=5, numcol=5):
		Frame.__init__(self, parent)
		self.numrow = numrow
		self.numcol = numcol
		self.makeWidgets(numrow, numcol)


