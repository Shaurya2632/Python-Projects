def GST(total):
    return total * 5 / 100

print("Welcome, what would you like to order?")

menu = {
    "coffee": 250,
    "cake": 500,
    "lassi": 50
}

total = 0

item_1 = input("Item name: ").lower()

if item_1 in menu:
    total += menu[item_1]
else:
    print("The item is out of stock")

add_item = input("Add another item? (yes/no): ").lower()

if add_item == "yes":
    item_2 = input("Item name: ").lower()
    if item_2 in menu:
        total += menu[item_2]
    else:
        print("The item is out of stock")

gst_amount = GST(total)
final_total = total + gst_amount

print()
print(f"Your bill is {final_total} (including GST of {gst_amount})")


