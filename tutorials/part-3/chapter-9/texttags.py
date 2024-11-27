"demo advanced tag and text interfaces"

from tkinter import *
root = Tk()
def hello(event):
	print("Got event : %s" % event)

text = Text()
text.config(font=("courier", 15, "normal"))
text.config(width=20, height=12)
text.pack(expand=YES, fill=BOTH)
text.insert(END, "This is \n\n the meaning\n\nof life.\n\n")

btn = Button(text, text="Spam",command=lambda: hello(""))
btn.pack()
text.window_create(END, window=btn)
text.insert(END, "\n\n")
img = PhotoImage(file="../chapter-8/pics/five.gif")
text.image_create(END,image=img)

text.tag_add("demo", "1.5", "1.7")
text.tag_add("demo1", "3.1", "3.4")
text.tag_add("demo2", "5.3", "5.7")

text.tag_config("demo", background = "purple")
text.tag_config("demo1", foreground = "red")
text.tag_config("demo2", font=("times", 16, "underline"))
text.tag_bind("demo", "<Double-1>", hello)
root.mainloop()