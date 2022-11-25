def dictionary_operations(sequence):
    my_dictionary = {}
    for items in range(0, len(sequence), 2):
        key = sequence[items]
        value = int(sequence[items + 1])
        my_dictionary[key] = value
    return my_dictionary


def stock_checker(dictionary, inputs):
    if inputs in dictionary:
        quantity = dictionary[inputs]
        print(f"We have {quantity} of {inputs} left")
    else:
        print(f"Sorry, we don't have {inputs}")


input_string = input().split(" ")
result = dictionary_operations(input_string)
input_checks = input().split(" ")
for items in input_checks:
    stock_checker(result, items)
