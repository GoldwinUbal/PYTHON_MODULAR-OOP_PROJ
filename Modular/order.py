# order.py

from menu import menu, display_menu


def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower().strip()

        if answer == "yes" or answer == "no":
            return answer

        print("Please enter only yes or no.")


def take_order():
    orders = []

    while True:
        display_menu()

        item = input("Enter the item you want to order: ").title().strip()

        if item not in menu:
            print("Sorry, that item is not on the menu.")
            print("Please choose an item from the menu.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid whole number.")

        price = menu[item]
        item_total = price * quantity
        orders.append([item, quantity, price, item_total])

        print(f"{quantity} {item}(s) added to your order.")

        another = get_yes_no(
            "Do you want to order another item? (yes/no): "
        )

        if another == "no":
            break

    return orders
