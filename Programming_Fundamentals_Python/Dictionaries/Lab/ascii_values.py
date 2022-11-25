list_of_characters = input().split(", ")
dictionary_of_characters = {key:ord(key) for key in list_of_characters}
print(dictionary_of_characters)