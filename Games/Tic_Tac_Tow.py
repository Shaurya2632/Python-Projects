import os, random, sys
from rich.table import Table # type: ignore
from rich.console import Console # type: ignore
from rich import box # type: ignore
from rich.text import Text # type: ignore
from rich.panel import Panel
from rich.rule import Rule

Tic_Tac_Tow = [" " for _ in range(9)]

Win_Combos = [[0,1,2], [3,4,5], [6,7,8], 
              [0,3,6], [1,4,7], [2,5,8], 
              [0,4,8], [2,4,6]]

Symbols = {
  0:"O",
  1:"X",
  "X":"O",
  "O":"X"
}

Players = {}

Ply1 = ""
Ply2 = ""

def Layout():
   
   global Tic_Tac_Tow

   console = Console()

   table = Table(show_header=False, show_lines=True, box=box.ROUNDED)

   for _ in range(3):
       table.add_column(style="yellow", width=7)
       
   for i in range(0, 9, 3):  
        table.add_row(f"\n   {Tic_Tac_Tow[i]} \n", f"\n   {Tic_Tac_Tow[i+1]} \n", f"\n   {Tic_Tac_Tow[i+2]} \n")
   
   console.print(table)

def Checker(Tic_Tac_Tow):
  
  global Players, Ply1, Ply2, Win_Combos
  
  # Check for a win
  for k, v in Players.items():
     for combo in Win_Combos:
         if all(Tic_Tac_Tow[i] == v for i in combo):
             os.system("cls")
             Layout()
             print(f"{k} Won The Game\n")
             cont = input("Continue (T/F): ").lower()

             if cont == "t":
                 Reset()
             else:
                 sys.exit()
  
  # Check for a draw
  if " " not in Tic_Tac_Tow:
      os.system("cls")
      Layout()
      print("Match Is Draw")
      cont = input("Continue (T/F): ").lower()

      if cont == "t":
          Reset()
      else:
          sys.exit()

def DashBoard():
   
   dashBoard = Table(show_header=False, show_lines=True, box=box.SQUARE)
   
   dashBoard.add_column(style="yellow")
   
   dashBoard.add_row(f"{Ply1}",  f"{Players[Ply1]}")
   dashBoard.add_row(f"{Ply2}",  f"{Players[Ply2]}")
   
   Console().print(dashBoard)   

def init(choice):
  global Players, Symbols, Ply1, Ply2
  if choice == 1:
    Players.update({"Computer": Symbols[random.choice([0,1])]})
    Players.update({"You": Symbols[Players["Computer"]]})
    
    Ply1 = "Computer"
    Ply2 = "You" 
    
  elif choice == 2: 
    Ply1, Ply2 = input("\nEnter Players Name: ").split(", ")
    
    Players.update({Ply1: Symbols[random.choice([0,1])]})
    Players.update({Ply2: Symbols[Players[Ply1]]}) 
  
def Reset():
  os.system("cls")
  global Tic_Tac_Tow, Players, Ply1, Ply2
  
  for i in range(len(Tic_Tac_Tow)): Tic_Tac_Tow[i] = " "
  Players.clear()
  Ply1 = ""
  Ply2 = ""
  Controller()
  
def Controller():
  os.system("cls")
  
  options = Panel("1. Player VS Computer\n2. Player VS Player\n\n")
  
  Console().print(options)
  
  choice  = int(input("Enter Choice: "))
  
  init(choice) 
  mainGame()
  
def Computer_Algorhythm():
    global Tic_Tac_Tow, Win_Combos, Players
    
    # First try to win
    for combos in Win_Combos:
      
        # Check if computer can win in this combo
        computer_count = 0
        empty_pos = None
        for pos in combos:
            if Tic_Tac_Tow[pos] == Players["Computer"]:
                computer_count += 1
            elif Tic_Tac_Tow[pos] == " ":
                empty_pos = pos
        
        # If two computer symbols and one empty space, take the win
        if computer_count == 2 and empty_pos is not None:
            return empty_pos
    
    # Block opponent from winning
    for combos in Win_Combos:
        # Check if player is about to win
        player_count = 0
        empty_pos = None
        for pos in combos:
            if Tic_Tac_Tow[pos] == Players["You"]:
                player_count += 1
            elif Tic_Tac_Tow[pos] == " ":
                empty_pos = pos
        
        # If two player symbols and one empty space, block it
        if player_count == 2 and empty_pos is not None:
            return empty_pos
   
    if  Tic_Tac_Tow[4] == " ":
        return 4
    
    # Take a corner if available
    corners = [0, 2, 6, 8]
    empty_corners = [pos for pos in corners if Tic_Tac_Tow[pos] == " "]
    if empty_corners:
        return random.choice(empty_corners)
    
    # Take any available space
    empty_spaces = [i for i, spot in enumerate(Tic_Tac_Tow) if spot == " "]
    if empty_spaces:
        return random.choice(empty_spaces)
    
    # If no moves available (should never reach here in a proper game)
    return None
  
def mainGame():

   while True:
      os.system("cls") 
      DashBoard()
      Layout()
         
      if Ply1 == "Computer":
         # Player's turn
         valid_move = False
         while not valid_move:
            try:
               You = int(input(f"{Ply2}r Turn (1-9): "))
               if You < 1 or You > 9:
                  print("Please enter a number between 1 and 9.")
                  continue
               
               if Tic_Tac_Tow[You-1] != " ":
                  print("That position is already taken. Try again.")
                  continue
                  
               Tic_Tac_Tow[You-1] = Players["You"]
               valid_move = True
            except ValueError:
               print("Please enter a valid number.")
               
         Checker(Tic_Tac_Tow)

         # Computer's turn
         Computer = Computer_Algorhythm()
         
         if Computer is not None:
            Tic_Tac_Tow[Computer] = Players["Computer"]

         Checker(Tic_Tac_Tow)
           
      else: 
         # Player 1's turn
         valid_move = False
         while not valid_move:
            try:
               p1 = int(input(f"{Ply1}'s Turn (1-9): "))
               if p1 < 1 or p1 > 9:
                  print("Please enter a number between 1 and 9.")
                  continue
               
               if Tic_Tac_Tow[p1-1] != " ":
                  print("That position is already taken. Try again.")
                  continue
                  
               Tic_Tac_Tow[p1-1] = Players[Ply1]
               valid_move = True
            except ValueError:
               print("Please enter a valid number.")
               
         os.system("cls")
         DashBoard()
         Layout()      
               
         Checker(Tic_Tac_Tow)      
         
         # Player 2's turn
         valid_move = False
         while not valid_move:
            try:
               p2 = int(input(f"{Ply2}'s Turn (1-9): "))
               if p2 < 1 or p2 > 9:
                  print("Please enter a number between 1 and 9.")
                  continue
               
               if Tic_Tac_Tow[p2-1] != " ":
                  print("That position is already taken. Try again.")
                  continue
                  
               Tic_Tac_Tow[p2-1] = Players[Ply2]
               valid_move = True
            except ValueError:
               print("Please enter a valid number.")
   
      os.system("cls")
      DashBoard()
      Layout()
  
      Checker(Tic_Tac_Tow)
               
Controller()                    