import time, os, sys, pyttsx3, random
from rich.table import Table
from rich.console import Console
from rich import box
from rich.progress import Progress

engine = pyttsx3.init()
engine.setProperty('rate', 170)
text = " "
Balance = 0

def TextToSpeech(text):
   engine.say(text)    
   engine.runAndWait()
   
def ProfressBar():
    with Progress(transient=True) as progress:
              task = progress.add_task("[green]Processing...  ", total=100)
              rand = random.randint(1, 3) / 5
              for _ in range(100):
                   time.sleep(rand)
                   progress.update(task, advance=1)     

while True:
    
    os.system("cls")
    
    table = Table(show_lines=True, show_edge=True, box=box.ROUNDED)
    
    table.add_column("N", style="Yellow")
    table.add_column("Bank", style="white", width=10)
    
    table.add_row("1", "Deposit")
    table.add_row("2", "Withdraw")
    table.add_row("3", "Exit")
    table.add_row("", "")
    
    table.add_row("B", f"{Balance}")

    Console().print(table)

    choice = int(input("choice: "))

    if choice == 1:
        Deposit = float(input("\nAmount: "))
        ProfressBar()
        Balance += Deposit
    
        TextToSpeech(text) 

    elif choice == 2:
        withdraw_amount = float(input("\nAmount: "))

        if  withdraw_amount <= Balance:
            ProfressBar()
            Balance -= withdraw_amount
        
        else: text = "insufficient Balance"
        
        TextToSpeech(text)   
              
    elif choice == 3:
        time.sleep(4)
        TextToSpeech("Thanks for using")
        print('exiting....') 
        time.sleep(2)
        os.system("cls")
        sys.exit()
        
    else:
        print("invalid choice")
