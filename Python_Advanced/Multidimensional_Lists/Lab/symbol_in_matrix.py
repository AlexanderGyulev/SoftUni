rows_and_columns = int(input())

matrix = list()

found_flag = False

for iterations in range(rows_and_columns):
    curr_list = []
    current_input = input()
    for element in current_input:
        curr_list.append(element)
    matrix.append(curr_list)

needed_symbol = input()

for el in range(len(matrix)):
    if found_flag:
        break
    for curr_el in matrix[el]:
        if curr_el == needed_symbol:
            position = matrix[el].index(curr_el)
            found_flag = True
            print(f"({el}, {position})")
            break

if not found_flag:
    print(f"{needed_symbol} does not occur in the matrix")
