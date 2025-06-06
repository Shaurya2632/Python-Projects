
from playsound import playsound
import time, sys
from rich.console import Console 
from rich.panel import Panel
from rich.progress import Progress

def Play(path):
    playsound(path)

class Vehicle:

     name = ""
     maxSpeed = 0
     tyre = 0
     cost = 0.0
     driver = ""
     numberPlate = ""
     company = ""
     fuelCapacity = 0
     currentFuel = 0
     speed = 0
     odoMeter = 0

     engineHeat = 30
     engineHeatIncreaseRate = 5
     fuelDrainPerKm = 1

     speed_Record = []

     VehicleType = ""
     
     VehicleInfo = ""

     def __init__(self, vehicleType, company, name, numberPlate, maxSpeed, fuel_Capacity, tyre, cost):

         self.company = company
         self.VehicleType = vehicleType
         self.name = name
         self.numberPlate = numberPlate
         self.maxSpeed = maxSpeed
         self.fuelCapacity = fuel_Capacity
         self.tyre = tyre
         self.cost = cost

         self.fuelCapacity = str(self.fuelCapacity) + "L"

         self.VehicleInfo = (
                             "[bold]Vehicle Type[/bold]   : " + self.VehicleType + "\n"
                             "[bold]Company[/bold]        : " + self.company + "\n"
                             "[bold]Name[/bold]           : " + self.name + "\n"
                             "[bold]Number Plate[/bold]   : " + self.numberPlate + "\n"
                             "[bold]Tyres[/bold]          : " + str(self.tyre) + "\n"
                             "[bold]Max Speed[/bold]      : " + str(self.maxSpeed) + "\n"
                             "[bold]Fuel Capacity[/bold]  : " + str(self.fuelCapacity) + "\n"
                             "[bold]Price[/bold]          : " + f"{self.cost:,}"
                               )

    
         self.fuelCapacity = int(self.fuelCapacity.replace("L", ""))

     def addFuel(self, fuel):
         self.currentFuel = fuel

     def engineON(self):

         if self.currentFuel > 5:  print(f"{self.name} Started"), Play(r"D:\coding\python\Sounds\Car Start.mp3")
         elif self.currentFuel > 2: print("Fuel is in Reserved, Please Refuel")
         else: print("No Fuel")

     def engineOff(self, reason = "User stoped"):
         Play(r"D:\coding\python\Sounds\Car Stop.mp3"), print(f"{self.name} Stoped ({reason})")

         if reason.lower() != "user stoped": sys.exit()

     def fuelLevel(self):
         print(self.currentFuel)

     def drive(self, speed=1, acceleration=1):

         if self.currentFuel == 0: self.engineOff("Out of Fuel")
         if speed > self.maxSpeed or self.engineHeat > 100: self.engineOff("engine Load")

         if speed < self.speed: acceleration = -acceleration

         self.speed_Record.append(speed)
         self.odoMeter += 1

         time.sleep(((speed - self.speed) / acceleration)/4)

         self.speed = speed

         if len(self.speed_Record) >= 2:
          if (abs(self.speed_Record[-1] - self.speed_Record[-2])) > 15: self.engineOff("Gear Shaft B")

         self.engineHeat += self.engineHeatIncreaseRate
         print(fr"{self.name} driving at {self.speed} Km\H")
         self.fuelDrainPerKm = self.speed * 0.05
         self.currentFuel -= self.fuelDrainPerKm

     def info(self):
         self.fuelCapacity = str(self.fuelCapacity) + "L"

         Console().print(Panel(self.VehicleInfo, title="[bold]Vehicle Info[/bold]", border_style="bold green", expand=True))

         self.fuelCapacity = int(self.fuelCapacity.replace("L", ""))

     def distance(self):
         print(f"{self.odoMeter} Km")

     def repair(self, damage):
         
         with Progress(transient=True) as progress:
              task = progress.add_task("[green]Repairing...", total=100)
              for _ in range(100):
                   time.sleep((damage/1000) * 0.1)  # Simulate cleaning time
                   progress.update(task, advance=1)

         Console().print("Vehicle repaired")

     def overDrive(self):

       print(f"{self.name} OverDrive Mode Started"),  Play(r"D:\coding\python\Sounds\OverDrive.mp3")
       self.maxSpeed *= 3
       self.fuelDrainPerKm = self.speed * 0.05
       self.engineHeatIncreaseRate = 10

     def coolDown(self, sec=3):

         self.speed = 0

         with Progress(transient=True) as progress:
              task = progress.add_task("[green]CoolDowing...    ", total=100)
              for _ in range(100):
                   time.sleep(sec/100)  # Simulate cleaning time
                   self.engineHeat -= 5
                   progress.update(task, advance=1)

         self.engineHeatIncreaseRate = 5
         Console().print("Cool Down Completed")

car = Vehicle("Sports Car", "Ford", "Mustang", "MH346996FG", 300,45, 4, 60600000)
car.info()