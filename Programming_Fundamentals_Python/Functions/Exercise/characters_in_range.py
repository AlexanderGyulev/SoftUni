first_character = input()
second_character = input()


def characters(a, b):
    a = ord(a) + 1
    b = ord(b)
    list_characters = []
    for items in range(a, b):
        list_characters.append(chr(items))
    return list_characters


result = characters(first_character, second_character)
print(*result, sep=" ")
