# menu.py

menu = {
    "Burger": 120,
    "Fries": 60,
    "Chicken": 150,
    "Spaghetti": 100,
    "Soft Drink": 50
}


def display_menu():
    print("\n========== MENU ==========")

    for item, price in menu.items():
        print(f"{item:<15} PHP {price:.2f}")

    print("==========================\n")
