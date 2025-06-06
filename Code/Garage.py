
import os, sys
from rich.table import Table
from rich import box
from rich.console import Console
from rich.prompt import Prompt

store = {
    "Battery": 1000,
}

item = {
    "Battery": 10
}
profit = 0
balance = 20000
car_repaired = 0
issues = {
    "discharged battery": 5000,
    "tyre puncture": 1000
}

customer = []

def Owner():
    
    global store, balance, car_repaired, profit
    
    table = Table(show_lines=True, box=box.SQUARE, show_header=False)
        
    table.add_column(style="Yellow")
        
    table.add_row("Balance", f"{balance}")
    table.add_row("Car Repaired", f"{car_repaired}")
    table.add_row("Profit", f"{profit}")
        
    items = Table(show_lines=True, box=box.SQUARE, show_header=False) 
        
    items.add_column(style="Yellow")
        
    for product, QYT in item.items(): 
            
        items.add_row(product, f"{QYT} QYT")
            
        if item: Console().print(items)
            
        balance += profit
        
        Console().print(table)
        buy_item = input("buy item: ")

        if buy_item == "yes":
            item_name = input("item name: ").lower()
            quantity = int(input("quantity: "))
            
            if item_name or quantity in store:
                print(store[item_name])
                total_price = store[item_name] * quantity
                
                if balance > total_price:
                    item[item_name] = store[item_name]
                    balance -= store[item_name]
                    
                elif balance < total_price:
                    print("Insufficient balance.")
                    
            else:
                print("item is out of stock")

pruductReqirementOnIssue = {
    "discharged battery": "Battery",
    "tyre puncture": "tyre"
}

while True:
    
    os.system("cls")
    
    user_type = input("Owner / Customar: ").lower()
    
    if user_type == "owner": Owner()
        
        
    elif user_type == "customer":
        
        ask = lambda text: Prompt.ask(text)
        
        name = ask("Name")
        customer.append(name)
        
        table = Table(show_lines=True, box=box.SQUARE)
        
        table.add_column("Issue", style="Yellow")
        table.add_column("Price", style="white")
        
        for issue, price in issues.items():
            table.add_row(issue.title(), f'{price}')
            
        Console().print(table)    
        
        UserIssue = input("\nIssue: ").lower()
        
        if UserIssue in issues: 
            
           if item[pruductReqirementOnIssue[UserIssue]]:
               print("\nIssue Solved")
               car_repaired += 1
               item[pruductReqirementOnIssue[UserIssue]] -= 1
               
               profit += issues[UserIssue]
               balance += profit
               
           else: 
               print("\nSorry, The Requried Item Is Not Available")     
        

    #     if issue_ in issue:
    #         if item['battery'] > 0:
    #             print(balance)
    #             item['battery'] -= 1
    #             car_repaired += 1
    #             print("Car repaired successfully.")
    #             print(f"Your bill is {issue[issue_]}.")
    #         elif item['battery'] == 0:
    #             print("the item is out of stock")
    #     else:
    #         print("Issue not found in our records.")
    # else:
    #     print("Invalid input. Please choose 'owner' or 'customer'.")
