
from playsound import playsound
import time, sys

def Play(path):
    playsound(path)

def repair(damage):
    time.sleep(1000/damage)


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

     def __init__(self, vehicleType, company, name, numberPlate, maxSpeed, fuel_Capacity, tyre, cost):

         self.company = company
         self.VehicleType = vehicleType
         self.name = name
         self.numberPlate = numberPlate
         self.maxSpeed = maxSpeed
         self.fuelCapacity = fuel_Capacity
         self.tyre = tyre
         self.cost = cost

         with open(fr"D:\coding\python\Models\Data\{self.name}.txt", "w") as f:

             self.fuelCapacity = str(self.fuelCapacity) + "L"

             f.write(f"""
             +----------------------------------------+
             | Vehicle Type  : {self.VehicleType:<22} |
             |----------------------------------------|
             | Company       : {self.company:<18}     |
             | Name          : {self.name:<15}        |
             | Number Plate  : {self.numberPlate:<22} |
             | Tyres         : {self.tyre:<15}        |
             | Max Speed     : {self.maxSpeed:<19}    |
             | Fuel Capacity : {self.fuelCapacity:<19}    |
             | Price         : {self.cost:<15,}        |
             +----------------------------------------+""")

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

         print(f"""
                      +----------------------------------------+
                      | Vehicle Type  : {self.VehicleType:<22} |
                      |----------------------------------------|
                      | Company       : {self.company:<18}     |
                      | Name          : {self.name:<15}        |
                      | Number Plate  : {self.numberPlate:<22} |
                      | Tyres         : {self.tyre:<15}        |
                      | Max Speed     : {self.maxSpeed:<19}    |
                      | Fuel Capacity : {self.fuelCapacity:<19}    |
                      | Price         : {self.cost:<15,}        |
                      +----------------------------------------+""")

         self.fuelCapacity = int(self.fuelCapacity.replace("L", ""))

     def distance(self):
         print(f"{self.odoMeter} Km")

     def repair(self, damage):
         time.sleep(1000/damage)
         print(f"{self.name} Repaired")

     def overDrive(self):

       print(f"{self.name} OverDrive Mode Started"),  Play(r"D:\coding\python\Sounds\OverDrive.mp3")
       self.maxSpeed *= 3
       self.fuelDrainPerKm = self.speed * 0.05
       self.engineHeatIncreaseRate = 10

     def coolDown(self, sec=3):

         self.speed = 0

         for i in range(1, sec+1):
             time.sleep(1)
             self.engineHeat -= 5
             print(f"{self.name} Cool Down Completed")
         self.engineHeatIncreaseRate = 5



car = Vehicle("Sports Car", "Ford", "Mustang", "MH346996FG", 300,45, 4, 60600000)
car.addFuel(40)
car.engineON()
car.drive(30)
car.drive(44)
car.drive(56)
car.drive(67)
car.drive(75)
car.drive(75)
car.drive(60)
car.drive(53)
car.drive(45)
car.drive(33)
car.drive(20)
car.drive(13)
car.drive(3)
car.coolDown()
car.drive(12)
car.drive(24)
car.drive(35)
car.drive(49)
car.overDrive()
car.drive(59)
car.engineOff()