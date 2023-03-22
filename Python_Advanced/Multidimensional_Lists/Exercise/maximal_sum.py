from sys import maxsize

rows, columns = map(int, input().split())

max_element = -maxsize

matrix = [list(map(int, input().split())) for _ in range(rows)]
max_el_matrix = []

for i in range(rows-2):
    for j in range(columns-2):
        el1 = matrix[i][j]
        el2 = matrix[i][j + 1]
        el3 = matrix[i][j + 2]
        el4 = matrix[i + 1][j]
        el5 = matrix[i + 1][j + 1]
        el6 = matrix[i + 1][j + 2]
        el7 = matrix[i + 2][j]
        el8 = matrix[i + 2][j + 1]
        el9 = matrix[i + 2][j + 2]
        current_sum = el1 + el2 + el3 + el4 + el5 + el6 + el7 + el8 + el9
        if max_element < current_sum:
            max_element = current_sum
            max_el_matrix.clear()
            max_el_matrix.append([el1, el2, el3])
            max_el_matrix.append([el4, el5, el6])
            max_el_matrix.append([el7, el8, el9])

print(f"Sum = {max_element}")
for index in range(len(max_el_matrix)):
    print(" ".join(str(x) for x in max_el_matrix[index]))
