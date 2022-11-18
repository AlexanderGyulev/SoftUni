numbers_input = input().split()

opposite_numbers = []

for element in numbers_input:
    element = int(element)
    if element > 0:
        element = -element
    else:
        element = abs(element)

    opposite_numbers.append(element)

print(opposite_numbers)
