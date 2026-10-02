# main.py
# Python OOP Version
# Python Exercise No. 2.1

from restaurant import Restaurant


def main():
    print("==========================================")
    print("       WELCOME TO MY RESTAURANT")
    print("==========================================")

    restaurant = Restaurant()

    choice = restaurant.get_yes_no(
        "Would you like to order? (yes/no): "
    )

    if choice == "yes":
        restaurant.take_order()
        restaurant.print_receipt()
    else:
        print("Thank you! Have a nice day. :)")


if __name__ == "__main__":
    main()
