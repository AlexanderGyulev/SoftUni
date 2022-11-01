def min_max_sum(sequence):
    integer_list = []
    for item in sequence:
        integer_list.append(int(item))
    min_integer = min(integer_list)
    max_integer = max(integer_list)
    sum_integers = sum(integer_list)
    return min_integer, max_integer, sum_integers


sequence_of_numbers = input().split(" ")
result = min_max_sum(sequence_of_numbers)
print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result[2]}")
