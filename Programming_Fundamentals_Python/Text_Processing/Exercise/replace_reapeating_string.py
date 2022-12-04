string_input = input()

new_string = ""

for elements in range(len(string_input)):
    current_letter = string_input[elements]
    if elements == 0:
        new_string += current_letter
    else:
        if current_letter != new_string[-1]:
            new_string += current_letter

print(new_string)
