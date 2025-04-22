
import os, pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 160)
text = ""

os.system("cls")
weight, height = input("Enter weight, height(in kg, cm): ").split(", ")

weight = float(weight)
height = float(height)

height /= 100

BMI = weight / height ** 2

print(f"\nYour BMI is: {round(BMI, 2)}")

if BMI <= 15: text = "You are underweight"
elif BMI <= 25: text = "You are normal weight"
elif BMI <= 30 : "You are overweight"
else: text = "You are obese"
engine.say(text)
engine.runAndWait()