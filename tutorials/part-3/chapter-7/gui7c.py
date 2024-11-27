import gui7
from tkinter import *

class HelloPackage(gui7.HelloPackage):
	def __getattr__(self, name):
		#print(name)
		#self.top.mainloop()
		return getattr(self.top,name)

if __name__ == '__main__':
	HelloPackage().mainloop()