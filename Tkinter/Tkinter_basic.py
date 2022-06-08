# Author :- Biresashis Das

import tkinter

windows = tkinter.Tk()
windows.title("My Fisrt GUI")
windows.minsize(width=600, height=600)

lable = tkinter.Label(text= "This is a Normal Text", font=("Arial",15,"bold"))
lable.pack(side="top")

windows.mainloop()



