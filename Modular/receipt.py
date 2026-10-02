# receipt.py


def print_receipt(orders, total, discount):
    final_total = total - discount

    print("\n==========================================")
    print("           MY RESTAURANT")
    print("              RECEIPT")
    print("==========================================")

    print(f"{'Item':<15}{'Qty':<6}{'Price':<10}{'Total':<10}")
    print("------------------------------------------")

    for order in orders:
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
