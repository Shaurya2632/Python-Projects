store = {
    "battery": 1000,
}

customer = []

item = {}
profit = 0
balance = 20000
car_repaired = 0
issue = {
    "discharged battery": 5000,
    "tyre puncture": 1000
}
while True:
    print('''''')
    user_type = input("Are you an 'owner' or a 'customer'? ").lower()
    if user_type == "owner":

        balance += profit
        print(f"your total balance is {balance}")
        print(f"Car repaired {car_repaired}")
        print(f"your profit is {profit}")
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
                    continue
            else:
                print("item is out of stock")
        else:
            continue
    elif user_type == "customer":
        name = input("your name: ")
        customer.append(name)
        issue_ = input("your issue: ").lower()

        if issue_ in issue:
            if item['battery'] > 0:
                print(balance)
                item['battery'] -= 1
                car_repaired += 1
                print("Car repaired successfully.")
                print(f"Your bill is {issue[issue_]}.")
            elif item['battery'] == 0:
                print("the item is out of stock")
        else:
            print("Issue not found in our records.")
    else:
        print("Invalid input. Please choose 'owner' or 'customer'.")
