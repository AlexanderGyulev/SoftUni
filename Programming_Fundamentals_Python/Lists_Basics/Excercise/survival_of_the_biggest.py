list_of_integers = input().split(" ")
count_of_numbers_to_remove = int(input())

integer_list = []

for numbers in list_of_integers:
    current_number = int(numbers)
    integer_list.append(current_number)

for elements in range(count_of_numbers_to_remove):
    smallest_int = min(integer_list)
    integer_list.remove(smallest_int)

for ints in range(len(integer_list)):
    if ints < len(integer_list) - 1:
        print(integer_list[ints], end=", ")
    else:
        print(integer_list[ints])