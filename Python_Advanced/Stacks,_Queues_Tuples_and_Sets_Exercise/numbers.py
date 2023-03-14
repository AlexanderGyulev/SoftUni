first_sequence_of_integers = set(map(int, input().split()))
second_sequence_of_integers = set(map(int, input().split()))

lines_of_input = int(input())

for _ in range(lines_of_input):
    current_command = input()
    if "Add First" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                first_sequence_of_integers.add(int(element))
    elif "Add Second" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                second_sequence_of_integers.add(int(element))
    elif "Remove First" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                element = int(element)
                first_sequence_of_integers.discard(element)
    elif "Remove Second" in current_command:
        split_command = current_command.split(" ")
        for element in split_command:
            if element.isdigit():
                element = int(element)
                second_sequence_of_integers.discard(element)
    elif "Check Subset" in current_command:
        if first_sequence_of_integers.issubset(second_sequence_of_integers):
            print(True)
        elif second_sequence_of_integers.issubset(first_sequence_of_integers):
            print(True)
        else:
            print(False)

first_sequence_of_integers = sorted(first_sequence_of_integers)
second_sequence_of_integers = sorted(second_sequence_of_integers)

print(*first_sequence_of_integers, sep=", ")
print(*second_sequence_of_integers,sep=", ")

