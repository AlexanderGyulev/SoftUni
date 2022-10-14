total_numbers = int(input())

numbers_list = []
after_command_list = []

for nums in range(total_numbers):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()

for i in range(len(numbers_list)):
    if command == "even":
        if numbers_list[i] % 2 == 0:
            after_command_list.append(numbers_list[i])
    elif command == "odd":
        if numbers_list[i] % 2 != 0:
            after_command_list.append(numbers_list[i])
    elif command == "negative":
        if numbers_list[i] < 0:
            after_command_list.append(numbers_list[i])
    elif command == "positive":
        if numbers_list[i] >= 0:
            after_command_list.append(numbers_list[i])

print(after_command_list)
