first = set(map(int, input().split()))
second = set(map(int, input().split()))

lines_of_input = int(input())

for _ in range(lines_of_input):
    current_command = input()
    if "Add First" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                first.add(int(element))
    elif "Add Second" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                second.add(int(element))
    elif "Remove First" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                element = int(element)
                first.discard(element)
    elif "Remove Second" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                element = int(element)
                second.discard(element)
    elif "Check Subset" in current_command:
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
