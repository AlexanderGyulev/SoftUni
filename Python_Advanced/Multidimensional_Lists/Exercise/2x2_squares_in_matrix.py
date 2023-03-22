rows, columns = map(int, input().split())

matrix = []

for _ in range(rows):
    current_line = list(input().split())
    matrix.append(current_line)

counter = 0

for i in range(rows):
    for j in range(columns):
        if len(matrix[i]) > j + 1 and len(matrix) > i + 1:
            el1 = matrix[i][j]
            el2 = matrix[i][j + 1]
            el3 = matrix[i + 1][j]
            el4 = matrix[i + 1][j + 1]
            if el1 == el2 == el3 == el4:
                counter += 1
print(counter)
