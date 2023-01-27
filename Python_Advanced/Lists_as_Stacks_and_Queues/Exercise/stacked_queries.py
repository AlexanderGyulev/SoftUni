from collections import deque

number_of_operations = int(input())

stack_of_numbers = deque()

for _ in range(number_of_operations):
    current_command = input()
    if "1 " in current_command:
        append_element = int(current_command.split(" ")[1])
        stack_of_numbers.append(append_element)
    elif current_command == "2":
        if len(stack_of_numbers) >= 1:
            stack_of_numbers.pop()
    elif current_command == "3":
        if len(stack_of_numbers) >= 1:
            max_num = max(stack_of_numbers)
            print(max_num)
    elif current_command == "4":
        if len(stack_of_numbers) >= 1:
            min_num = min(stack_of_numbers)
            print(min_num)

stack_of_numbers.reverse()
print(*stack_of_numbers, sep=", ")
