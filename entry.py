from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
	goldfish = "Hello " + e.get()
	myLabel = Label(root, text=goldfish)
	myLabel.pack()

myButton = Button(root, text="Enter name", command=myClick, fg="green", bg="white")
myButton.pack()

root.mainloop()
