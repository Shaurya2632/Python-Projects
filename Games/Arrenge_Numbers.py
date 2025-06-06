import random
from customtkinter import *
from CTkTable import CTkTable
import numpy as np

def to2D(li, rows, cols):
    return np.array(li).reshape(rows, cols).tolist()

def fill():
    global Board
    numbers = [str(n) for n in range(1, 9)] + [" "]
    random.shuffle(numbers)
    Board = numbers

def shift(key):
    global Board, curEle
    curPos = Board.index(curEle)

    if key == "up" and curPos >= 3 and Board[curPos - 3] == " ":
        Board[curPos], Board[curPos - 3] = " ", curEle
    elif key == "down" and curPos <= 5 and Board[curPos + 3] == " ":
        Board[curPos], Board[curPos + 3] = " ", curEle
    elif key == "left" and curPos % 3 != 0 and Board[curPos - 1] == " ":
        Board[curPos], Board[curPos - 1] = " ", curEle
    elif key == "right" and curPos % 3 != 2 and Board[curPos + 1] == " ":
        Board[curPos], Board[curPos + 1] = " ", curEle

def changeEle(key):
    global curEle
    if key.isdigit() and key in [str(n) for n in range(1, 9)]:
        curEle = key

def check_win():
    if Board == winPos:
        print("You Win!")
        Game.destroy()
        sys.exit()

def on_key(event):
    key = event.keysym.lower()
    if key in ["up", "down", "right", "left"]:
        shift(key)
    elif key.isdigit() and key in [str(n) for n in range(1, 9)]:
        changeEle(key)
    elif key == "escape":
        print("Exiting...")
        Game.destroy()
        sys.exit()

    table.configure(values=to2D(Board, 3, 3))

    check_win()

# ------------------- Main --------------------

Board = [" " for _ in range(9)]
curEle = "1"
winPos = ["1", "2", "3", "6", "5", "4", "7", "8", " "]

fill()

curPos = Board.index(curEle)

Game = CTk()
Game.bind("<Key>", on_key)

table = CTkTable(
    master=Game,
    row=3,
    column=3,
    values=to2D(Board, 3, 3),
    height=50,
    width=50,
    font=("Arial", 25),
    corner_radius=1
)

table.place(x=20, y=20)

Game.mainloop()
