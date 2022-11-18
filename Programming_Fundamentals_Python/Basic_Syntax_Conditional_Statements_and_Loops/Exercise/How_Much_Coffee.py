current_command = input()
total_number_coffees = 0

while current_command != "END":
    if current_command == "coding" or current_command == "dog" or current_command == "cat" \
            or current_command == "movie":
        total_number_coffees += 1
    elif current_command == "CODING" or current_command == "DOG" or current_command == "CAT" \
            or current_command == "MOVIE":
        total_number_coffees += 2
    if total_number_coffees > 5:
        break
    current_command = input()

if total_number_coffees > 5:
    print("You need extra sleep")
else:
    print(total_number_coffees)