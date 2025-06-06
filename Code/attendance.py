
import os, pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 250)

def cls():
    os.system("cls")

present = 0
absent = 0
P_Roll = []
A_Roll = []
text = ""

print("Start Attendance....\n")

i = 1

while(i <= 25):
    cls()
    text = f"Roll No {i}" 
    engine.say(text), engine.runAndWait()
    
    P_A = input(f"{text} = ").lower()
    
    if P_A == "p":
        present += 1
        P_Roll.append(i)
    elif P_A == "a":
        absent += 1
        A_Roll.append(i)
    if P_A == "p" or P_A == "a": i += 1
    
cls()    
text = "Attendance Completed"
print(f"{text}\n")    

engine.say(text)
engine.runAndWait()
    
print(f"Total Present = {present}")
print(f"Total Absent = {absent}\n")

print(f"Present Roll NOs = {P_Roll}")

print(f"Absent Roll NOs = {A_Roll}\n")