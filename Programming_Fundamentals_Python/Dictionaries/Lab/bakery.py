def dictionary_operations(sequence):
    my_dictionary = {}
    for items in range(0, len(sequence), 2):
        dict_key = sequence[items]
        dict_value = int(sequence[items + 1])
        my_dictionary[dict_key] = dict_value
    return my_dictionary


input_string = input().split(" ")
result = dictionary_operations(input_string)
print(result)
