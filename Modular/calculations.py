# calculations.py


def calculate_total(orders):
    total = 0

    for order in orders:
        total += order[3]

    return total


def calculate_discount(total):
    if total >= 500:
        discount = total * 0.10
    elif total >= 300:
        discount = total * 0.05
    else:
        discount = 0

    return discount
