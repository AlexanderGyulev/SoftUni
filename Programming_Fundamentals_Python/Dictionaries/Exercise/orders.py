prices_dictionary = {}
quantity_dictionary = {}
while True:
    command = input()
    if command == "buy":
        break
    current_command = command.split()
    product = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])
    if product not in quantity_dictionary:
        quantity_dictionary[product] = 0
    prices_dictionary[product] = price
    quantity_dictionary[product] += quantity

for keys, values in prices_dictionary.items():
    quantities = int(quantity_dictionary[keys])
    total_price = values * quantities
    print(f"{keys} -> {total_price:.2f}")
