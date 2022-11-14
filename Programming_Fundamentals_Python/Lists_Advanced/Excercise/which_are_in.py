def find_substrings(first_sequence, second_sequence):
    final_list = []
    for items in first_sequence:
        for elements in second_sequence:
            if items in elements:
                final_list.append(items)
                break
    return final_list


first_input_line = input().split(", ")
second_input_line = input().split(", ")
result = find_substrings(first_input_line, second_input_line)
print(result)
