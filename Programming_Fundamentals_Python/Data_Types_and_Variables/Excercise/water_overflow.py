number_of_inputs = int(input())

total_liters = 0

for lines in range(number_of_inputs):
    current_number = int(input())
    if total_liters + current_number > 255:
        print("Insufficient capacity!")
        continue
    total_liters += current_number

print(total_liters)
