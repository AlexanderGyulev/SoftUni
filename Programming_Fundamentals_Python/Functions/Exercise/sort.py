def to_int(some_list):
    final_list = []
    for item in some_list:
        final_list.append(int(item))
    return final_list


sequence_of_numbers = input().split(" ")
integers = to_int(sequence_of_numbers)
result = sorted(integers)
print(result)
