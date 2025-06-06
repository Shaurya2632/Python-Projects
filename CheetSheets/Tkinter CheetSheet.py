# import all things from tkinter file
from tkinter import *

# creating Obj of Tkinter

win = Tk()

# for remove any thing

win.destroy()

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

win.attributes("-alpha", 0.6) # for translucent
win.attributes("-fullscreen", 0.6) # for enter to full screen

# for give minimum and maximum window size

win.minsize(100, 100)
win.maxsize(500, 500)

# for stop resize GUI

win.resizable(False, False)

# make text in tkinter using

text = Label(win, text = "This is Text")

# for change mouse cursor when it points on text

text = Label(win, text = "This is Text", cursor = "plus")

# for customize text in tkinter

text = Label(win, text = "This is Text", relief = "raised")

# for justify text in tkinter

text = Label(win, text = "This is Text", justify = "center")

# use textVariable for run time text update

var = StringVar()

text = Label(win, textvariable = var, justify = "center")

var.set("Hello World")

# use underline to give underline in text
text = Label(win, "This is Text", underline = 2)

# add text in GUI

text.pack()
text.grid()
text.place()

# for give external padding in gui

text.pack(padx = 100, pady = 90)

# for give internal padding

text.pack(ipadx = 100, ipady=90)

# for fill the text to till width

text.pack(ipadx = 100, ipady=90, fill='x')
text.pack(ipadx = 100, ipady=90, fill='y')

# for align text

text2 = Label(win, "This is Text")

text2.pack(side = "top")

# use expend for expend

text2.pack(expand = True)

# set row, column in gird

text2.grid(row = 4, column = 6)

# give row and column span

text.grid(rowspan = 3, columnspan = 7)

# give x and y in place

text2.place(x = 4, y = 8)

# there are 4 type of tkinter variables

var1 = StringVar()
var2 = IntVar()
var3 = BooleanVar()
var4 = DoubleVar()

# for get or set tkinter var values

var1.set(56)
var1.get()

# for use image (only png)

photo = PhotoImage(file = r"filePath")

# use image in label

label = Label(win, image = photo)

# for use text with image

label = Label(win, image = photo, text = "My Text", compound = "top")

# for use label with frame

label_frame = LabelFrame(win, text = "My Text", font = 100)

# adjust label in labelFrame

label_frame = LabelFrame(win, text = "My Text", font = 100, labelanchor = N)
label_frame.place(x = 100, y = 100, height = 100, width = 500)

# for use button in tkinter

button = Button(win, text = "On", font = ("Arial", 30))
button.place(x = 100, y = 100, height = 100, width = 500)

# use font color in button
# use all things that are in label and label Frame

button = Button(win, text = "On", font = ("Arial", 30), fg = "yellow")

# for making working button

button = Button(win, text = "On", font = ("Arial", 30), fg = "yellow", compound = "FunctionName")

# making checkbox in tkinter

checkBox = Checkbutton(win, text = "start", font = 30, variable = var)

# set on and off value in checkbox

checkBox = Checkbutton(win, text = "start", font = 30, variable = var, onvalue = "", offvalue = "")

# get checkbox with blank

checkBox.deselect()

# Running tkinter till clicking exit or close()

# use menu Button in tkinter

menuButton = Menubutton(win, text = "select")
menuButton.menu = Menu(menuButton)
menuButton["menu"] = menuButton

# add list items in men button

menuButton.menu.add_checkbutton(label = "Red")

win.mainloop()
