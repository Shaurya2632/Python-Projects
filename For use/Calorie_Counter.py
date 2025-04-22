
import os, sys

Total_Calorie = 0 
exit = False

Calorie_Per_Food = {
    # Main meals
    "roti"            : lambda w, qty: round((297 / 100) * w * qty, 2),
    "rice"            : lambda w, qty: round((130 / 100) * w * qty, 2),
    "dal"             : lambda w, qty: round((116 / 100) * w * qty, 2),
    "paneer"          : lambda w, qty: round((265 / 100) * w * qty, 2),
    "rajma"           : lambda w, qty: round((140 / 100) * w * qty, 2),
    "aloo sabzi"      : lambda w, qty: round((120 / 100) * w * qty, 2),
    "poha"            : lambda w, qty: round((130 / 100) * w * qty, 2),
    "upma"            : lambda w, qty: round((120 / 100) * w * qty, 2),
    "idli"            : lambda w, qty: round((58 / 100)  * w * qty, 2),
    "sambar"          : lambda w, qty: round((70 / 100)  * w * qty, 2),
    "dosa"            : lambda w, qty: round((165 / 100) * w * qty, 2),
    "curd"            : lambda w, qty: round((60 / 100)  * w * qty, 2),
    "chole"           : lambda w, qty: round((150 / 100) * w * qty, 2),
    "paratha"         : lambda w, qty: round((300 / 100) * w * qty, 2),
    "biryani"         : lambda w, qty: round((160 / 100) * w * qty, 2),
    "khichdi"         : lambda w, qty: round((120 / 100) * w * qty, 2),
    "thepla"          : lambda w, qty: round((200 / 100) * w * qty, 2),
    "dhokla"          : lambda w, qty: round((160 / 100) * w * qty, 2),
    "khandvi"         : lambda w, qty: round((100 / 100) * w * qty, 2),
    "vegetable curry" : lambda w, qty: round((90 / 100)  * w * qty, 2),
    "mutter paneer"   : lambda w, qty: round((180 / 100) * w * qty, 2),
    "aloo tikki"      : lambda w, qty: round((130 / 100) * w * qty, 2),
    "veg pulao"       : lambda w, qty: round((150 / 100) * w * qty, 2),

    # Raw ingredients
    "wheat"           : lambda w, qty: round((340 / 100) * w * qty, 2),
    "rice (raw)"      : lambda w, qty: round((365 / 100) * w * qty, 2),
    "jowar"           : lambda w, qty: round((349 / 100) * w * qty, 2),
    "bajra"           : lambda w, qty: round((361 / 100) * w * qty, 2),
    "ragi"            : lambda w, qty: round((336 / 100) * w * qty, 2),
    "barley"          : lambda w, qty: round((354 / 100) * w * qty, 2),
    "quinoa"          : lambda w, qty: round((368 / 100) * w * qty, 2),
    "corn"            : lambda w, qty: round((365 / 100) * w * qty, 2),
    "moong dal"       : lambda w, qty: round((347 / 100) * w * qty, 2),
    "urad dal"        : lambda w, qty: round((341 / 100) * w * qty, 2),
    "chana dal"       : lambda w, qty: round((370 / 100) * w * qty, 2),

    # Snacks / street food
    "vada pav"        : lambda w, qty: round((290 / 100) * w * qty, 2),
    "samosa"          : lambda w, qty: round((262 / 100) * w * qty, 2),
    "pav bhaji"       : lambda w, qty: round((240 / 100) * w * qty, 2),
    "sev puri"        : lambda w, qty: round((200 / 100) * w * qty, 2),
    "bhel puri"       : lambda w, qty: round((150 / 100) * w * qty, 2),
    "dahi puri"       : lambda w, qty: round((180 / 100) * w * qty, 2),
    "khaman"          : lambda w, qty: round((160 / 100) * w * qty, 2),
    "bhajiya"         : lambda w, qty: round((280 / 100) * w * qty, 2),
    "veg cutlet"      : lambda w, qty: round((170 / 100) * w * qty, 2),
    "bread butter"    : lambda w, qty: round((250 / 100) * w * qty, 2),
    "bread jam"       : lambda w, qty: round((275 / 100) * w * qty, 2),
    "misal pav"       : lambda w, qty: round((250 / 100) * w * qty, 2),
    "sabudana khichdi": lambda w, qty: round((200 / 100) * w * qty, 2),
    "handvo"          : lambda w, qty: round((150 / 100) * w * qty, 2),
    "thalipeeth"      : lambda w, qty: round((220 / 100) * w * qty, 2),

    # Sweets
    "halwa (suji)"    : lambda w, qty: round((300 / 100) * w * qty, 2),
    "kheer"           : lambda w, qty: round((120 / 100) * w * qty, 2),
    "ladoo (besan)"   : lambda w, qty: round((450 / 100) * w * qty, 2),
    "gulab jamun"     : lambda w, qty: round((320 / 100) * w * qty, 2),
    "rasgulla"        : lambda w, qty: round((186 / 100) * w * qty, 2),
    "jalebi"          : lambda w, qty: round((350 / 100) * w * qty, 2),
    "modak"           : lambda w, qty: round((250 / 100) * w * qty, 2),
    "shrikhand"       : lambda w, qty: round((210 / 100) * w * qty, 2),
    "barfi"           : lambda w, qty: round((400 / 100) * w * qty, 2),

    # Fruits
    "banana"          : lambda w, qty: round((89 / 100) * w * qty, 2),
    "apple"           : lambda w, qty: round((52 / 100) * w * qty, 2),
    "mango"           : lambda w, qty: round((60 / 100) * w * qty, 2),
    "orange"          : lambda w, qty: round((47 / 100) * w * qty, 2),
    "grapes"          : lambda w, qty: round((69 / 100) * w * qty, 2),

    # Dry fruits & nuts
    "almond"         : lambda w, qty: round((579 / 100) * w * qty, 2),
    "cashew"         : lambda w, qty: round((553 / 100) * w * qty, 2),
    "raisin"         : lambda w, qty: round((299 / 100) * w * qty, 2),
    "walnut"         : lambda w, qty: round((654 / 100) * w * qty, 2),
    "date"           : lambda w, qty: round((282 / 100) * w * qty, 2),
}

def Cal_Counter(food, weight, qyt):
  
  if food in Calorie_Per_Food:
    return Calorie_Per_Food[food](weight, qyt)
  else: return "Sorry, Food Not Found In Food Calorie Chart, We Will Add it Soon"
  
def inputer():
  
  try: 
      food = input("Enter Food Name: ").strip().lower()
      weight = float(input("Enter Food weight: "))
      QYT = int(input("Enter Food QYT: "))
      
  except ValueError: return ValueError["Error Aquried"]    
  
  return Cal_Counter(food, weight, QYT)
  
def Controller():
  
  global Total_Calorie, exit
  
  Count = 9 - len(str(Total_Calorie))

  spaces = ""
  
  for i in range(1, Count): spaces += " "  
  
  menu = f"""

+------------------------------+
|     Food Calorie Counter     |
|------------------------------|
| Total Calorie: {Total_Calorie} cal {spaces} |
|------------------------------|

"""

  confermation = ["yes", "yea", "t", "true", "y", "continue"]

  if exit == True:
    print(menu)
    sys.exit()

  while (True):
  
     print(menu)
     Total_Calorie += inputer()
  
     addOrNot = input("\nAdd: ")
     print(Total_Calorie)
     
     os.system("cls")
  
     if addOrNot.lower() in confermation: Controller()
      
     else: 
       
       exit = True
       Controller()
     
Controller()     
  