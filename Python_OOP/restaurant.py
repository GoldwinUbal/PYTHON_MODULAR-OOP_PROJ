# restaurant.py
# Python OOP Version


class Restaurant:
    # menu
    def __init__(self):
        self.menu = {
            "Burger": 120,
            "Fries": 60,
            "Chicken": 150,
            "Spaghetti": 100,
            "Soft Drink": 50
        }
        self.orders = []

    def get_yes_no(self, prompt):
        while True:
            answer = input(prompt).lower().strip()

            if answer == "yes" or answer == "no":
                return answer

            print("Please enter only yes or no.")


    def display_menu(self):
        print("\n========== MENU ==========")

        for item, price in self.menu.items():
            print(f"{item:<15} PHP {price:.2f}")

        print("==========================\n")

    def take_order(self):
        while True:
            self.display_menu()

            item = input(
                "Enter the item you want to order: "
            ).title().strip()

            if item not in self.menu:
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

            price = self.menu[item]
            item_total = price * quantity
            self.orders.append([item, quantity, price, item_total])

            print(f"{quantity} {item}(s) added to your order.")

            another = self.get_yes_no(
                "Do you want to order another item? (yes/no): "
            )

            if another == "no":
                break

    def calculate_total(self):
        total = 0

        for order in self.orders:
            total += order[3]

        return total

    #discount
    def calculate_discount(self, total):
        if total >= 500:
            discount = total * 0.10
        elif total >= 300:
            discount = total * 0.05
        else:
            discount = 0

        return discount

    # receipt
    def print_receipt(self):
        total = self.calculate_total()
        discount = self.calculate_discount(total)
        final_total = total - discount

        print("\n==========================================")
        print("           MY RESTAURANT")
        print("              RECEIPT")
        print("==========================================")

        print(f"{'Item':<15}{'Qty':<6}{'Price':<10}{'Total':<10}")
        print("------------------------------------------")

        for order in self.orders:
            item = order[0]
            quantity = order[1]
            price = order[2]
            item_total = order[3]

            print(
                f"{item:<15}{quantity:<6}"
                f"PHP {price:<7.2f}PHP {item_total:.2f}"
            )

        print("------------------------------------------")
        print(f"Subtotal:                  PHP {total:.2f}")
        print(f"Discount:                  PHP {discount:.2f}")
        print(f"Total:                     PHP {final_total:.2f}")
        print("==========================================")
        print("       Thank you for ordering!")
        print("==========================================\n")
