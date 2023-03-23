rows, columns = map(int, input().split())

matrix = []

for index in range(97, 97 + rows):
    first_el = chr(index)
    current_list = []
    for el in range(index, index + columns):
        second_el = chr(el)
        current_element = first_el + second_el + first_el
        current_list.append(current_element)
    matrix.append(current_list)

for i in range(len(matrix)):
    print(f"{' '.join(str(x) for x in matrix[i])}")
