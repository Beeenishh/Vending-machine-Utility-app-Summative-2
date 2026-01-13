#Vending machine items and prices
items = {
    "Chips": {
        "1": {"name": "Lays Classic", "price": 4.50},
        "2": {"name": "Doritos", "price": 12.50},
        "3": {"name": "Pringles", "price": 7.00}
    },

    "Chocolates": {
        "4": {"name": "Snickers", "price": 3.75},
        "5": {"name": "KitKat", "price": 4.25},
        "6": {"name": "Dairy Milk", "price": 1.50}
    },

    "Drinks": {
        "7": {"name": "Soda", "price": 2.00},
        "8": {"name": "Water", "price": 1.00},
        "9": {"name": "Juice", "price": 1.50}
    }
}

def display_menu(items):
    print("Welcome to Beenish's Vending Machine!")
    print("Please select an item:")

    for category, products in items.items():
        print(f"\n-- {category} --")
        for code, item in products.items():
            print(f"{code}. {item['name']} - AED {item['price']}")

def find_selected_item(items, selection):
    for products in items.values():
        if selection in products:
            return products[selection]
    return None


#created a loop to have the customer add multiple items before checking out.
while True:
    #Display available items
    display_menu(items)

    #Ask customer for input
    selection = input("Enter the item number you wish to purchase: ")

    #Find selected item using function
    selected_item = find_selected_item(items, selection)

    if selected_item:
        print(f"You have selected {selected_item['name']}.")
        amount_due = selected_item['price']

        #Requesting the customer to insert money
        while amount_due > 0:
            try:
                payment = float(input(f"Please insert AED {amount_due:.2f}: "))
                if payment >= amount_due:
                    change = payment - amount_due
                    print(f"Thank you for your purchase! Your change is AED {change:.2f}.")
                    print(f"{selected_item['name']} has been dispensed. Enjoy your {selected_item['name']}!")
                    break
                else:
                    print("Insufficient payment. Please insert more money.")
                    amount_due -= payment
            except ValueError:
                print("Invalid payment amount. Please enter a valid number.")
    else:
        print("Invalid selection. Please try again.")

    #Ask if customer wants another item
    again = input("Would you like to buy another item? (yes/no thanks): ").strip().lower()
    if again != "yes":
        print("Thank you for using Beenish's Vending Machine! :)")
        break
