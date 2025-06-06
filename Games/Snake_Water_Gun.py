import random

computer = random.choice([-1, 0, 1])

dict_Choice = {
  "s": 1,
  "w": -1,
  "g": 0
}
reveDict = {
  1: "Snake",
  -1: "Water",
  0: "Gun"
}

user = dict_Choice[input("Enter your Choice: ")]

print(f"You Chose {reveDict[user]}\nComputer chose {reveDict[computer]}")

if computer == user: print("Draw")
    
else:
   if computer == -1 and user == 1:print("User Win")
   elif computer == -1 and user == 0:print("Computer Win")
   elif computer == 1 and user == 0:print("User Win")
   elif computer == 1 and user == -1:print("Computer Win")
   elif computer == 0 and user == 1: print("Computer Win")
   elif computer == 0 and user == -1:print("User Win")
   else: print("Something Went Wrong")
