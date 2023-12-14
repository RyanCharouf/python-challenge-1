menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49},
}

order_list = []

while True:
    print("Menu:")
    for key, item in menu_items.items():
        print(f"{key}. {item['Item name']} - ${item['Price']:.2f}")

    menu_selection = input("Enter your selection (1-3): ")

    try:
        menu_selection = int(menu_selection)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    if menu_selection not in menu_items.keys():
        print("Error: Invalid selection. Please choose a valid item.")
        continue

    item_name = menu_items[menu_selection]["Item name"]

    quantity = input(f"How many {item_name}s would you like? (default is 1): ")

    try:
        quantity = int(quantity) if quantity.isdigit() else 1
    except ValueError:
        quantity = 1

    order_list.append({
        "Item name": item_name,
        "Price": menu_items[menu_selection]["Price"],
        "Quantity": quantity,
    })

    place_order = input("Would you like to order anything else? (y/n): ").lower()

    if place_order == 'y':
        continue
    elif place_order == 'n':
        print("Thank you for your order!")
        break
    else:
        print("Error: Invalid input. Please enter 'y' or 'n'.")
        continue

print("\nOrder Receipt:")
print(f"{'Item name':<25} | {'Price':<6} | {'Quantity'}")
print("-" * 40)

for order in order_list:
    item_name, price, quantity = order["Item name"], order["Price"], order["Quantity"]
    spaces_name = ' ' * (25 - len(item_name))
    spaces_price = ' ' * (6 - len(f"${price:.2f}"))
    print(f"{item_name}{spaces_name} | ${price:.2f}{spaces_price} | {quantity}")

total_price = sum(order["Price"] * order["Quantity"] for order in order_list)
print("\nTotal Price: ${:.2f}".format(total_price))
