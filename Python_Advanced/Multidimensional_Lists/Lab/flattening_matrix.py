matrix_rows = int(input())

main_matrix = []

for iterations in range(matrix_rows):
    curr_list = map(int, input().split(", "))
    for element in curr_list:
        main_matrix.append(element)

print(main_matrix)
