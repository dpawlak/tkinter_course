from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="green", bg="white")
myButton.pack()

root.mainloop()
