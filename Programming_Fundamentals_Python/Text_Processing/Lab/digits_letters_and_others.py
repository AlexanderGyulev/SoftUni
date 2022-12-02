string_input = input()

digit_list = []
letters_list = []
character_list = []

for elements in string_input:
    if elements.isalpha():
        letters_list.append(elements)
    elif elements.isdigit():
        digit_list.append(elements)
    else:
        character_list.append(elements)

print(*digit_list, sep="")
print(*letters_list, sep="")
print(*character_list, sep="")
