def even_operations(sequence):
    integers_list = list(map(int, sequence))
    final_list = [num for num in range(len(integers_list)) if integers_list[num] % 2 == 0]
    return final_list


string_of_numbers = input().split(", ")
final_result = even_operations(string_of_numbers)
print(final_result)
