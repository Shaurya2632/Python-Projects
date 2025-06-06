import sys, os, random, numpy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Utility, time, keyboard

def toSeries(li):
  
    return [item for row in li for item in row]

def toMatrix(li):
  
  return numpy.array(li).reshape(5, 5).tolist()

def fill():
  
    global Board
    
    Board[random.randint(0, 4)][random.randint(0, 4)] = head

def create_board():
  
  global Board
  
  print(f"┌{"─" * 11}┐")
  
  for i in range(5):
  
       print("│", end=" ")
       
       for j in range(5):
           
           print(Board[i][j], end=" ")
           
       print("│")  
       
  print(f"└{"─" * 11}┘")     
  
def extendSnake():
    
    global Board, arrow
    
    if arrow == "up":
      
      Board = toSeries(Board)
      data = Utility.util.matrixPos(Board.index(head), 5)
      Board = toMatrix(Board)
      
      if data[0] + 2 > 5:
        data[0] = 1
      
      Board[data[0]+1][data[1]] = parts
          
def reset():
  
  global Board
  
  Board = numpy.array([" " for _ in range(25)]).reshape(5, 5).tolist()
          
head = "■"
parts = "●"
arrow = "up"
arrows = ["up", "down", "right", "left"]

Board = numpy.array([" " for _ in range(25)]).reshape(5, 5).tolist()

while True:
       
     os.system("cls")
     fill()
     extendSnake()
     extendSnake()
     create_board()
     reset()
  