import random, os, sys
import keyboard
from rich import box
from rich.table import Table
from rich.console import Console

curEle = "●"
curPos = 0

elements = {
    "C": "●",
    "S": "■",
    "Z": "$"
}

Board = [" " for _ in range(9)]

def show_board():

    global Board, elements
    
    rprint =  lambda str: Console().print(str)
    
    Dashboard = Table(show_lines=True, box = box.SQUARE, header_style= "blue bold")
    
    Dashboard.add_column("Elements")
    Dashboard.add_column("Keys")
    
    for i, j in elements.items():
    
       Dashboard.add_row(f"{j}", f"{i}" , style= "bold" if curEle == j else "dim")
    
    rprint(Dashboard)

    print( "┌───┬───┬───┐")
    print(f"│ {Board[0]} │ {Board[1]} │ {Board[2]} │")
    print( "├───┼───┼───┤")
    print(f"│ {Board[3]} │ {Board[4]} │ {Board[5]} │")
    print( "├───┼───┼───┤")
    print(f"│ {Board[6]} │ {Board[7]} │ {Board[8]} │")
    print( "└───┴───┴───┘")

def fill():

    global Board

    numbers = list(range(1, 9)) + [0]
    random.shuffle(numbers)
    Board = numbers

def tempFill():

    global Board, elements
    
    Board = [" " for _ in range(9)]
    
    leftNumbers = [1,2,3,4,5,6,7,8]
    
    for ele in elements.values():

       forFill = random.choice(leftNumbers)
       Board[forFill] = ele
       leftNumbers.remove(forFill)  

def shift(key):

    global Board, curPos, curEle

    curPos = Board.index(curEle)

    if key == "up" and curPos >= 3 and Board[curPos-3] == " ":
        Board[curPos], Board[curPos - 3] = " ", curEle

    elif key == "down" and curPos <= 5 and Board[curPos+3] == " ":
        Board[curPos], Board[curPos + 3] = " ", curEle

    elif key == "left" and curPos % 3 != 0 and Board[curPos-1] == " ":
        Board[curPos], Board[curPos - 1] = " ", curEle

    elif key == "right" and curPos % 3 != 2 and Board[curPos+1] == " ":
        Board[curPos], Board[curPos + 1] = " ", curEle

    elif key == "esc":
        print("Exiting...")      
        sys.exit()
    
def changeEle(key):
    
     global curEle
     
     eles = elements.keys()
     
     if key in eles: curEle = elements[key.upper()]
         
def controller():
    
     while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            key = event.name
            break
    
     if key in ["up", "down", "right", "left"]:
         shift(key) 
     
     else:
         changeEle(key)            
    
tempFill()

while True:
    
    os.system("cls")
    show_board()
       
    controller()

