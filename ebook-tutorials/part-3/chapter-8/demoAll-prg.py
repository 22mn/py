"""
4 demo classes run as independent program processes: command lines;
if one window is quit now, the others will live on; there is no simple way to
run all report calls here (though sockets and pipes could be used for IPC), and 
some launch schemes may drop child program stdout and disconnect parent/child;
"""
import sys
sys.path.append(r"D:\SANDBAG\PROGRAMMING\git-contribution\py\ebook-tutorials\part-2\chapter-5")

from tkinter import *
from launchmodes import PortableLauncher

demoModules = ["demoDlg", "demoRadio", "demoCheck", "demoScale"]

for demo in demoModules:
	PortableLauncher(demo, demo + ".py")()

root = Tk()
root.title("Process")
Label(root, text="Multiple program demo: command lines", bg="white").pack()
root.mainloop()