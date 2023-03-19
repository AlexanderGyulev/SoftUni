rows, columns = map(int, input().split(", "))

matrix = []

for elements in range(rows):
    curr_element = list(map(int, input().split()))
    matrix.append(curr_element)

for iteration in range(columns):
    curr_sum = 0
    for element in range(rows):
        curr_sum += matrix[element][iteration]
    print(curr_sum)
