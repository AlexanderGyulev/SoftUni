from collections import deque

string_of_colors = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}

final_list = []

# orange = red + yellow
# purple = red + blue
# green = yellow + blue

while string_of_colors:
    if len(string_of_colors) == 1:
        first = string_of_colors.pop()
        second = ""
    else:
        first = string_of_colors.pop()
        second = string_of_colors.popleft()
    current_string = first + second
    current_string_reversed = second + first
    if current_string in colors:
        final_list.append(current_string)
    elif current_string_reversed in colors:
        final_list.append(current_string_reversed)
    else:
        for element in (first[:-1], second[:-1]):
            if element:
                string_of_colors.insert(len(string_of_colors) // 2, element)

if "orange" in final_list:
    if "red" not in final_list or "yellow" not in final_list:
        final_list.remove("orange")
elif "purple" in final_list:
    if "red" not in final_list or "blue" not in final_list:
        final_list.remove("purple")
elif "green" in final_list:
    if "yellow" not in final_list or "blue" not in final_list:
        final_list.remove("green")

print(final_list)
