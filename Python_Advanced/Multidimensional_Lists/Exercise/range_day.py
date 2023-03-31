matrix = []

start_pos = []

move_commands = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

total_targets = 0
killed_targets = []
all_targets_down = False

for index in range(5):
    current_input = input().split()
    matrix.append(current_input)
    if "A" in current_input:
        x = current_input.index("A")
        start_pos = [index, x]
        matrix[index][x] = "."
    if "x" in current_input:
        total_targets += current_input.count("x")

number_of_inputs = int(input())
current_pos = start_pos

for elements in range(number_of_inputs):
    if len(killed_targets) == total_targets:
        all_targets_down = True
        break
    if all_targets_down:
        break
    commands_input = input().split()
    command = commands_input[0]
    direction = commands_input[1]
    if len(commands_input) == 3:
        steps = int(commands_input[2])
    else:
        steps = 0
    if command == "move":
        new_row = current_pos[0] + (move_commands[direction][0] * steps)
        new_col = current_pos[1] + (move_commands[direction][1] * steps)
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix) and matrix[new_row][new_col] == ".":
            current_pos = [new_row, new_col]
    elif command == "shoot":
        bullet_pos = current_pos
        new_bul_row = current_pos[0]
        new_bul_col = current_pos[1]
        while 0 <= new_bul_row < len(matrix) and 0 <= new_bul_col < len(matrix):
            if matrix[bullet_pos[0]][bullet_pos[1]] == "x":
                matrix[bullet_pos[0]][bullet_pos[1]] = "."
                killed_targets.append([bullet_pos[0], bullet_pos[1]])
                break
            else:
                new_bul_row = bullet_pos[0] + move_commands[direction][0]
                new_bul_col = bullet_pos[1] + move_commands[direction][1]
                bullet_pos = [new_bul_row, new_bul_col]

if total_targets > len(killed_targets):
    print(f"Training not completed! {total_targets - len(killed_targets)} targets left.")
else:
    print(f"Training completed! All {total_targets} targets hit.")

print(*killed_targets, sep="\n")
