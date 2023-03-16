rows, columns = map(int, input().split(", "))

matrix = []
total_sum = 0

for row_index in range(rows):
    current_input = list(map(int, input().split(", ")))
    matrix.append(current_input)

for curr_list in matrix:
    total_sum += sum(curr_list)

print(total_sum)
print(matrix)
