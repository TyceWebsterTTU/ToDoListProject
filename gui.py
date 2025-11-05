from tkinter import *

root = Tk()
root.title("To-Do List")
root.minsize(200, 200)
root.geometry("350x200")

lbl = Label(root, text = "Welcome to the To-Do List! Are you making a new list or adding to an existing one?")
lbl.grid()

btn1 = Button(root, text = "Making new list")
btn1.grid(column=2, row=0)

btn2 = Button(root, text = "Editing existing list")
btn2.grid(column=2, row=1)

root.mainloop()