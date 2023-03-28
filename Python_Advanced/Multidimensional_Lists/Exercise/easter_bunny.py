size_of_field = int(input())

matrix = []

paths_dict = {'up': [], 'down': [], 'left': [], 'right': []}
values_dict = {'up': [], 'down': [], 'left': [], 'right': []}

total_eggs_collected = 0
bunny_pos = []

for element in range(size_of_field):
    current_list = input().split()
    if "B" in current_list:
        bunny_index = current_list.index("B")
        bunny_pos = [element, bunny_index]
    matrix.append(current_list)

bunny_current_pos = bunny_pos

# eggs above bunny
for row in range(size_of_field):

    if 0 <= bunny_current_pos[0] - row < len(matrix) and 0 <= bunny_current_pos[1] < len(matrix):
        x = bunny_current_pos[0] - row
        if matrix[x][bunny_current_pos[1]] == "X":
            break
        elif matrix[x][bunny_current_pos[1]].isdigit():
            paths_dict['up'].append([x, bunny_current_pos[1]])
            values_dict['up'].append(int(matrix[x][bunny_current_pos[1]]))
    else:
        break

# eggs below bunny
for row in range(size_of_field):

    if 0 <= bunny_current_pos[0] + row < len(matrix) and 0 <= bunny_current_pos[1] < len(matrix):
        x = bunny_current_pos[0] + row
        if matrix[x][bunny_current_pos[1]] == "X":
            break
        elif matrix[x][bunny_current_pos[1]].isdigit():
            paths_dict['down'].append([x, bunny_current_pos[1]])
            values_dict['down'].append(int(matrix[x][bunny_current_pos[1]]))
    else:
        break

# right side of bunny

for col in range(size_of_field):

    if 0 <= bunny_current_pos[1] + col < len(matrix) and 0 <= bunny_current_pos[0] < len(matrix):
        x = bunny_current_pos[1] + col
        if matrix[bunny_current_pos[0]][x] == "X":
            break
        elif matrix[bunny_current_pos[0]][x].isdigit():
            paths_dict['right'].append([bunny_current_pos[0], x])
            values_dict['right'].append(int(matrix[bunny_current_pos[0]][x]))
    else:
        break

# left side of bunny
for col in range(size_of_field):

    if 0 <= bunny_current_pos[1] - col < len(matrix) and 0 <= bunny_current_pos[0] < len(matrix):
        x = bunny_current_pos[1] - col
        if matrix[bunny_current_pos[0]][x] == "X":
            break
        elif matrix[bunny_current_pos[0]][x].isdigit():
            paths_dict['left'].append([bunny_current_pos[0], x])
            values_dict['left'].append(int(matrix[bunny_current_pos[0]][x]))
    else:
        break

max_value = 0
max_path = ""

for keys, values in values_dict.items():
    sum_values = sum(values)
    if sum_values > max_value:
        max_value = sum_values
        max_path = keys
print(max_path)

for elements in paths_dict[max_path]:
    print(elements)

print(max_value)
