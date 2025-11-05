from tkinter import *

root = Tk()
root.title("To-Do List")
root.minsize(200, 200)
root.geometry("750x700")

lbl = Label(root, text = "Welcome to the To-Do List! Are you making a new list, adding to an existing one, or removing a list?")
lbl.grid()

btn1 = Button(root, text = "Make new list")
btn1.grid(column=2, row=0)

btn2 = Button(root, text = "Edit existing list")
btn2.grid(column=3, row=0)

btn3 = Button(root, text = "Remove list")
btn3.grid(column=4, row=0)


root.mainloop()