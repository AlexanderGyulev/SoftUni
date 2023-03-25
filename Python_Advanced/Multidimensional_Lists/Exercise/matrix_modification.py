rows = int(input())

matrix = []

for _ in range(rows):
    curr_line = list(map(int, input().split()))
    matrix.append(curr_line)

while True:
    current_command = input().split()
    if "END" in current_command:
        break
    cur_command = current_command[0]
    cur_row = int(current_command[1])
    cur_col = int(current_command[2])
    cur_value = int(current_command[3])
    if 0 > cur_row or cur_row > len(matrix) - 1:
        print("Invalid coordinates")
        continue
    if 0 > cur_col or cur_col > len(matrix[cur_row]) - 1:
        print("Invalid coordinates")
        continue
    if cur_command == "Add":
        old_el = matrix[cur_row][cur_col]
        matrix[cur_row][cur_col] = cur_value + old_el
    elif cur_command == "Subtract":
        old_el = matrix[cur_row][cur_col]
        matrix[cur_row][cur_col] = old_el - cur_value

for i in range(len(matrix)):
    print(f"{' '.join(str(x) for x in matrix[i])}")
