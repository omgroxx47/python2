from tkinter import *
window=Tk()
def callback():
    print("Welcome")
btn = Button(window, text="Ok",command=callback)
btn.pack()
