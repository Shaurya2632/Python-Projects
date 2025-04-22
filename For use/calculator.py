
import pyttsx3, os, sys

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def sum(num1, num2):
    return num1 + num2
    
def sub(num1, num2):
    return num1 - num2
    
def mlti(num1, num2):
    return num1 * num2
    
def divi(num1, num2):
        if num2 == 0:
            return "\033[31mdisplay Error---------------- Division by zero is not allowed.\033[0m"
        else:
            return round(num1 / num2, 3)
    
def exponent(num1, num2):
    return num1 ** num2
    
def greater_than(num1, num2):
    return num1 > num2

def less_than(num1, num2):
    
    return num1 < num2

def calu(num1, opr, num2):
    if opr == '+': return sum(num1, num2)
    elif opr == '-': return sub(num1, num2)
    elif opr == '*': return mlti(num1, num2)
    elif opr == '/': return divi(num1, num2)
    elif opr == '**' or opr == '^': return exponent(num1, num2)
    elif opr == '>': return greater_than(num1, num2)
    elif opr == '<': return less_than(num1, num2)

def TextToSpeech(text):
   print(text)
   print()
   engine.say(text.replace('**', f"to the power of {num2}").replace('*', 'multiply by').replace('/', 'divided by').replace('-', 'minus').replace('>', 'is greater than').replace('<', 'is less than'))    
   engine.runAndWait()
   
while(True):
    
   os.system("cls")

   print("""
|------------------|     
|    Calculator    |
|------------------|
""")

   exp = input("Enter Equation: ")
   num1, opr, num2 = exp.split()

   if '.' in num1: num1 = float(num1)
   else: num1 = int(num1)
   if '.' in num2: num2 = float(num2)
   else: num2 = int(num2) 

   Ans = calu(num1, opr, num2)       
     
   if Ans == "" or num2 == 0:
     print("\n\033[31mdisplay Error ------------------- Invalid operator.\033[0m")

     text = "Answer Not Displayed Due to Error"
     engine.say(text)    
     engine.runAndWait()
     print()
     continue
     
   text = f"{num1} {opr} {num2} = {Ans}"
   
   print()
   TextToSpeech(text)
        