string_input = input().split(" ")
string_dictionary = {}
for elements in string_input:
    for items in elements:
        if items in string_dictionary.keys():
            string_dictionary[items] += 1
        else:
            string_dictionary[items] = 1

for letters in string_dictionary.keys():
    value = string_dictionary[letters]
    print(f"{letters} -> {value}")
