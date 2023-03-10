number_of_commands = int(input())

registration_set = set()

for _ in range(number_of_commands):
    direction, registration_number = input().split(", ")
    if direction == "IN":
        registration_set.add(registration_number)
    elif direction == "OUT":
        registration_set.remove(registration_number)

if len(registration_set) != 0:
    for element in registration_set:
        print(element)
else:
    print("Parking Lot is Empty")
