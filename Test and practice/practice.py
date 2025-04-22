from tkinter import *

win = Tk()


win.geometry(f"400x400")

label = Label(win, text = "Label", font={"Arial", 28, "Normal"}, bg="blue")

label.pack()

win.iconbitmap("D:/coding/Python/Calc.ico")

win.mainloop()