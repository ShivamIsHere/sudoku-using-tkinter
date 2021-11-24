from tkinter import *

def openWin():
    #one way
    #try both code by uncommenting them one by one (dont uncomment both way at the same time)
    #window=Tk()
    #oldwindow.destroy()

    #another way
    new_window=Toplevel() #in this case the older window will act as bottom and if it is closed the new window will also be closed along with it

oldwindow=Tk()
Button(oldwindow,text='open new window',command=openWin).pack()
oldwindow.mainloop()