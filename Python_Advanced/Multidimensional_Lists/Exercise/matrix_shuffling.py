rows, columns = map(int, input().split())

matrix = []

for _ in range(rows):
    current_list = list(input().split())
    matrix.append(current_list)

while True:
    current_command = input().split()
    if "END" in current_command:
        break
    if len(current_command) != 5:
        print("Invalid input!   ")
        continue

    row1 = int(current_command[1])
    column1 = int(current_command[2])
    row2 = int(current_command[3])
    column2 = int(current_command[4])

    if current_command[0] != "swap" or row1 > rows or row2 > rows or column1 > columns or column2 > columns \
            or row1 < 0 or row2 < 0 or column1 < 0 or column2 < 0:
        print("Invalid input!")
        continue
    el1 = matrix[row1][column1]
    el2 = matrix[row2][column2]
    matrix[row1][column1] = el2
    matrix[row2][column2] = el1

    for i in range(len(matrix)):
        print(f"{' '.join(str(x) for x in matrix[i])}")
