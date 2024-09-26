"""Dmart """
#Welc(ome to dmart
items = {"Curd": 60, "milk": 40, "cooldrink": 100, "Bread": 48, "jam": 120, "badam(200grms)": 250, "rice": 2500, "oil": 650}
 
cart = {}
 
def add_item(item_name, quantity):
    if item_name in cart:
        cart[item_name] += quantity
    else:
        cart[item_name] = quantity
 
def display_cart():
    if cart:
        print("Items in your cart:")
        print("{:<15}{:<10}{:<10}{:<10}".format("Item", "Quantity", "Price(₹)", "Total(₹)"))
        total_amount = 0
        for item, quantity in cart.items():
            price = items[item]
            total_item_price = price * quantity
            print("{:<15}{:<10}{:<10}{:<10}".format(item, quantity, price, total_item_price))
            total_amount += total_item_price 
        print("Total amount: ₹" + str(total_amount))
    else:
        print("Your cart is empty.")
 

while True:
    print("Available items in Dmart:")
    for item_name, price in items.items():
        print(item_name + ": ₹" + str(price))
    
    print("\n1. Add item to cart")
    print("2. View cart and total amount")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        item_name = input("Enter item name: ")
        if item_name in items:
            quantity = int(input("Enter quantity for " + item_name + ": "))
            add_item(item_name, quantity)
            print(str(quantity) + " x " + item_name + "(s) added to the cart.")
        else:
            print("Item not found. Please choose an available item.")
    
    elif choice == '2':
        display_cart()
    
    elif choice == '3':
        print("Exiting program. Thank you!")
        break
    
    else:
        print("Invalid choice. Please try again.")