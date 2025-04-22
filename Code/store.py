
import os, sys

menu = '''
|--------------------|
|  Welcome to Store  |
|--------------------|
| 1. Add Product     |
| 2. Remove Product  |
| 3. Exit            |
|--------------------|
'''

def addItem(items, Product_name, cart):
    price = items[Product_name] * 0.18
    cart.update({Product_name  : price})
    
def Clear():
    os.system('cls')


Items = {
    'smartphone': 30000,      'laptop': 50000,           'headphones': 1500,     'jeans': 2000,
    't-shirt': 500,           'dress': 3500,             'pizza': 500,           'burger': 250,
    'ice cream': 100,         'tablet': 20000,           'smartwatch': 8000,     'camera': 12000,
    'shoes': 3000,            'jacket': 2500,            'socks': 150,           'watch': 5000,
    'backpack': 1500,         'chocolate': 150,          'coffee': 100,          'sandwich': 200,
    'salad': 300,             'headset': 2500,           'keyboard': 1200,       'mouse': 500,
    'monitor': 8000,          'webcam': 2000,            'printer': 6000,        'scanner': 3500,
    'hard drive': 4000,       'USB drive': 800,          'charger': 600,         'tablet case': 1500,
    'phone case': 500,        'bluetooth speaker': 3000, 'earbuds': 1000,        'power bank': 1000,
    'gym equipment': 5000,    'yoga mat': 1000,          'bicycle': 10000,       'helmet': 1500,
    'skateboard': 2500,       'scooter': 8000,           'car': 1000000,         'motorcycle': 500000,
    'truck': 2000000,         'helicopter ride': 50000,  'plane ticket': 20000,  'train ticket': 1000,
    'bus ticket': 200,        'hotel stay': 5000,        'resort stay': 25000,   'spa treatment': 3000,
    'movie ticket': 300,      'concert ticket': 1500,    'sports ticket': 2000,  'museum ticket': 500,
    'theme park entry': 3000, 'book': 400,               'magazine': 150,        'e-book': 200,
    'notebook': 100,          'pen': 50,                 'pencil': 20,           'stapler': 300,
    'scissors': 100,          'paper': 200,              'calculator': 500,      'printer paper': 100,
    'post-its': 150,          'glue': 100,               'marker': 200,          'chalk': 50,
    'board eraser': 100,      'alarm clock': 500,        'lamp': 1000,           'fan': 1500,
    'air conditioner': 25000, 'heater': 3000,            'vacuum cleaner': 7000, 'washing machine': 15000,
    'microwave': 5000,        'fridge': 20000,           'oven': 8000,           'toaster': 1000,
    'blender': 2000,          'coffee maker': 1500,      'kettle': 500,          'iron': 1000,
    'sewing machine': 6000,   'telescope': 5000,         'binoculars': 1500,     'suitcase': 2500,
    'wallet': 500,            'belt': 1000,              'gloves': 300,          'scarf': 200,
    'hat': 500,               'sunglasses': 1000,        'umbrella': 300,        'swimsuit': 1500,
    'towel': 300,             'bedsheet': 1000,          'pillow': 500,          'mattress': 10000,
    'blanket': 1000,          'curtains': 2000,          'carpet': 5000
}
Cart = {}

Clear()
print(menu)
Choice = int(input('Choice: '))

if Choice == 3: 
    sys.exit()

exitP = 0

while exitP != 1:

     Item_Name = input('\nItem name: ').lower()

     if Item_Name in Items:
        addItem(Items, Item_Name, Cart)

     else:
        print('Item is out of stock')
        exitP = 1

     add_item = input('\nAdd item: ')

     if add_item == 'no':
        break

print('\nYour Order: \n')

for key, value in Cart.items():
    print(f'{key}, {value}')
    
print("\n")
      