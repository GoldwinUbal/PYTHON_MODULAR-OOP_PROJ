from order import take_order, get_yes_no
from calculations import calculate_total, calculate_discount
from receipt import print_receipt


def main():
    print("==========================================")
    print("       WELCOME TO MY RESTAURANT")
    print("==========================================")

    choice = get_yes_no("Would you like to order? (yes/no): ")

    if choice == "yes":
        orders = take_order()

        total = calculate_total(orders)
        discount = calculate_discount(total)

        print_receipt(orders, total, discount)

    else:
        print("Thank you! Have a nice day. :)")


if __name__ == "__main__":
    main()