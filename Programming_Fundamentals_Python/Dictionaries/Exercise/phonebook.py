phonebook_dictionary = {}
while True:
    command = input()
    if command.isdigit():
        break
    else:
        command = command.split("-")
        name = command[0]
        phone = command[1]
        phonebook_dictionary[name] = phone

for numbers in range(int(command)):
    name_to_search = input()
    if name_to_search in phonebook_dictionary:
        phone_num = phonebook_dictionary[name_to_search]
        print(f"{name_to_search} -> {phone_num}")
    else:
        print(f"Contact {name_to_search} does not exist.")
