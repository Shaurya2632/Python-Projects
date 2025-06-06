import builtins, re, time, winsound
from tkinter import *

def fixTime(format):
        numbers = re.findall(r"\d+", format)

        while len(numbers) < 3:
            numbers.insert(0, "0")

        hour, min, sec = map(int, (num.zfill(2) for num in numbers))

        hour = builtins.min(hour, 23)  # Limit hour to 23
        min = builtins.min(min, 59)  # Limit minute to 59
        sec = builtins.min(sec, 59)

        return f"{hour:02} : {min:02} : {sec:02}"

def formatToSecond(format):
    hour, min, sec = map(int, format.split(" : "))
    return hour * 3600 + min * 60 + sec

def secondToFormat(second):

    hour = second // 3600
    min = (second % 3600) // 60
    sec = second % 60

    return f"{hour:02} : {min:02} : {sec:02}"

def Timer():
    global userTime, win
    start.destroy()
    for i in range(formatToSecond(userTime)):
        userTime = secondToFormat(formatToSecond(userTime))
        time_var.set(userTime)
        userTime = secondToFormat(formatToSecond(userTime) - 1)
        win.update()
        time.sleep(1)

    time_var.set("Time's Up!")
    win.update()
    playBeep(10)

def playBeep(rep=3, dur=1):

    for i in range(1, rep+1):

        if i == rep: winsound.Beep(800, int(dur*100) + int(dur+400))
        else: winsound.Beep(800, int(dur*100))
        time.sleep(1)

    win.destroy()

userTime = input("Set Timer: ")

win = Tk()
win.title("Timer")
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")
win.resizable(False, False)
win.iconbitmap(r"E:\coding\python\Images\Timer.ico")

Title = Label(win, text="Timer", font=("Arial", 120, "bold"))
Title.place(x = 738, y = 50)

userTime = fixTime(userTime)

time_var = StringVar(win, value = userTime)

label = Label(win, textvariable=time_var, font=("Arial", 65, "normal"))
label.pack(expand = True)

start = Button(win, text = "Start", font = ("Arial", 50), relief = "groove",  command = Timer)
start.place(x = 1500, y = 460)

win.mainloop()
