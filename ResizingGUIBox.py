from tkinter import *
root=Tk()
root.geometry('1366x768')
height=IntVar()
width=IntVar()
heightvar=Entry(root,textvariable=height)
heightvar.pack()
widthvar=Entry(root,textvariable=width)
widthvar.pack()

def resizebox():
    root.geometry(f"{heightvar.get()}x{widthvar.get()}")
Button(text='resize',command=resizebox).pack()
root.mainloop()
