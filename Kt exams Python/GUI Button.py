from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello Python", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)
B1.pack()
top.mainloop()
