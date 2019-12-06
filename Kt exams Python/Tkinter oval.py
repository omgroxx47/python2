from tkinter import *
root=Tk()
c=Canvas (root,width=300,height=300)
c.pack()
c.create_oval(200,200,250,250,fill="red")
root.mainloop
