total_number_of_presents = int(input())
size = int(input())

matrix = []

santa_pos = []
total_good_kids = 0

good_kids_with_presents = 0

total_presents_given = 0

move_commands = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for index in range(size):
    current_list = input().split()
    if "S" in current_list:
        y = current_list.index("S")
        santa_pos = [index, y]
    if "V" in current_list:
        x = int(current_list.count("V"))
        total_good_kids += x
    matrix.append(current_list)

matrix[santa_pos[0]][santa_pos[1]] = "-"
current_santa_pos = santa_pos

while True:
    if total_number_of_presents == total_presents_given:
        matrix[current_santa_pos[0]][current_santa_pos[1]] = "S"
        break
    current_command = input()
    if "Christmas morning" in current_command:
        matrix[current_santa_pos[0]][current_santa_pos[1]] = "S"
        break
    a = move_commands[current_command][0]
    b = move_commands[current_command][1]
    if 0 <= current_santa_pos[0] + a < len(matrix) and 0 <= current_santa_pos[1] + b < len(matrix):
        current_santa_pos = [current_santa_pos[0] + move_commands[current_command][0],
                             current_santa_pos[1] + move_commands[current_command][1]]

        if matrix[current_santa_pos[0]][current_santa_pos[1]] == "V":
            good_kids_with_presents += 1
            total_presents_given += 1
            matrix[current_santa_pos[0]][current_santa_pos[1]] = "-"
        elif matrix[current_santa_pos[0]][current_santa_pos[1]] == "C":
            for value in move_commands.values():
                if total_number_of_presents == total_presents_given:
                    break
                temp_pos = [current_santa_pos[0] + value[0], current_santa_pos[1] + value[1]]
                if matrix[temp_pos[0]][temp_pos[1]] == "X":
                    matrix[temp_pos[0]][temp_pos[1]] = "-"
                    total_presents_given += 1
                elif matrix[temp_pos[0]][temp_pos[1]] == "V":
                    matrix[temp_pos[0]][temp_pos[1]] = "-"
                    good_kids_with_presents += 1
                    total_presents_given += 1
        elif matrix[current_santa_pos[0]][current_santa_pos[1]] == "X":
            matrix[current_santa_pos[0]][current_santa_pos[1]] = "-"

if total_presents_given == total_number_of_presents and total_good_kids > good_kids_with_presents:
    print("Santa ran out of presents!")

for index in range(len(matrix)):
    print(f"{' '.join(x for x in matrix[index])}")

if total_good_kids == good_kids_with_presents:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
elif total_good_kids > good_kids_with_presents:
    print(f"No presents for {total_good_kids - good_kids_with_presents} nice kid/s.")
