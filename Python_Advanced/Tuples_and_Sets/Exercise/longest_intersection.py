import sys

input_lines = int(input())

intersection_list = []

for _ in range(input_lines):
    current_input = input().split("-")
    first_start, first_end = map(int, current_input[0].split(","))
    second_start, second_end = map(int, current_input[1].split(","))
    first_set = set()
    second_set = set()
    first_counter = int(first_start)
    second_counter = int(second_start)
    while first_start <= first_counter <= first_end:
        first_set.add(first_counter)
        first_counter += 1
    while second_start <= second_counter <= second_end:
        second_set.add(second_counter)
        second_counter += 1
    final_tuple = tuple(first_set.intersection(second_set))
    if len(final_tuple) > len(intersection_list):
        intersection_list.clear()
        for items in final_tuple:
            intersection_list.append(items)

length = len(intersection_list)

print(f"Longest intersection is {intersection_list} with length {length}")
