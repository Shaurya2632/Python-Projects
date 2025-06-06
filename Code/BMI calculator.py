import Utility

from rich.table import Table
from rich.console import Console
from rich import box

text = ""

# os.system("cls")
weight, height = map(float, input("Enter weight(kg), height(cm): ").split(", "))

# os.system("cls")

BMI = Utility.BMICalculator(weight, height / 100)

table = Table(show_lines=True, box=box.SQUARE)

table.add_column("Unit", style="Blue")
table.add_column("Value", style="yellow")

table.add_row("Weight", f"{weight} Kg")
table.add_row("height", f"{height} Cm")
table.add_row("BMI", f"{round(BMI, 2)}")

Console().print(table)

if BMI <= 15: text = "underweight"
elif BMI <= 25: text = "normal weight"
elif BMI <= 30 : text = "overweight"
else: text = "obese"

Utility.speak(text)

