square_matrix_rows = int(input())

matrix = [list(map(int, input().split(" "))) for x in range(square_matrix_rows)]

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

first_diagonal = []
second_diagonal = []

for index in range(len(matrix)):
    curr_element = matrix[index][index]
    first_diagonal.append(curr_element)

for el in range(len(matrix)):
    curr_element = matrix[el][len(matrix) - 1 - el]
    second_diagonal.append(curr_element)

difference = abs(sum(first_diagonal) - sum(second_diagonal))

print(difference)
