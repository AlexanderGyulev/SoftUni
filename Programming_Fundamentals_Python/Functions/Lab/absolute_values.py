numbers = input().split(" ")

abs_numbers = []

for items in numbers:
    current_number = float(items)
    abs_numbers.append(abs(current_number))

print(abs_numbers)