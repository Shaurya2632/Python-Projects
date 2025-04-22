import time, os, sys, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)
text = " "
Balance = 0

def TextToSpeech(text):
   engine.say(text)    
   engine.runAndWait()

while True:
    
    os.system("cls")
    Blank = 16 - len(str(Balance))
    Spaces = ""
    
    i = 1
    
    while i < Blank:
         Spaces += ' '
         i += 1
    
    print(f'''
    |-------------------------|
    |     Bank management     |  
    |-------------------------|
    | 1. Deposit              | 
    | 2. Withdraw             | 
    | 3. Exit                 |
    |-------------------------|
    | Balance: {Balance}{Spaces}|
    |-------------------------|
     ''')

    choice = int(input("    choice: "))

    if choice == 1:
        Deposit = float(input("\n    deposit amount: "))
        Balance += Deposit
        text = "deposit successfully completed"
    
        time.sleep(1)
        
        TextToSpeech(text) 

    elif choice == 2:
        withdraw_amount = float(input("\n    withdrawal amount: "))

        if  withdraw_amount <= Balance:
            Balance -= withdraw_amount
            
            text = "withdraw successfully completed"
        
        else: text = "insufficient Balance"
        
        time.sleep(1)
        
        TextToSpeech(text)   
              
    elif choice == 3:
        time.sleep(4)
        TextToSpeech("Thanks for using")
        print('    exiting....') 
        time.sleep(2)
        os.system("cls")
        sys.exit()
        
    else:
        print("    invalid choice")
