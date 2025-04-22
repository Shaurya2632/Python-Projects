# import all things from tkinter file
from tkinter import *

# creating Obj of Tkinter

win = Tk()

# for give title of GUI

win.title("Your Title")

# for find system width

SYS_Width = win.winfo_screenwidth()

# for find system width

SYS_height = win.winfo_screenheight()

# formula to get center width

width = 600

center_width = int((SYS_Width - width)/2)

# formula to get center width

height = 700

center_height = int((SYS_height - height)/2)

# use icon to your GUI (filetype = .ico)

win.iconbitmap(r"D:\coding\python\Calc.ico")

# for give bg color of GUI

win.config(bg="blue")

# give attributes to the GUI

win.attributes("-alpha", 0.6)

# for give minimum and maximum window size

win.minsize(100, 100)
win.maxsize(500, 500)

# for stop resize GUI

win.resizable(False, False)

# Running tkinter till clicking exit or close()

win.mainloop()
