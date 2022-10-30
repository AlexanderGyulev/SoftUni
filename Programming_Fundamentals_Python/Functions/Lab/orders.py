product_name = input()
product_quantity = int(input())


def orders(name, quantity):
    if name == "coffee":
        price = 1.50
    elif name == "water":
        price = 1
    elif name == "coke":
        price = 1.40
    elif name == "snacks":
        price = 2
    price = price * quantity
    return price


print(f'{orders(product_name, product_quantity):.2f}')
