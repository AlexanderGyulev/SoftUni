statistics_dictionary = {}
while True:
    command = input()
    if command == "statistics":
        break
    key, value = command.split(": ")
    if key in statistics_dictionary:
        statistics_dictionary[key] += (int(value))
    else:
        statistics_dictionary[key] = int(value)

print("Products in stock:")
for keys, values in statistics_dictionary.items():
    print(f"- {keys}: {values}")

total_products = len(statistics_dictionary.keys())
total_quantity = sum(statistics_dictionary.values())
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
