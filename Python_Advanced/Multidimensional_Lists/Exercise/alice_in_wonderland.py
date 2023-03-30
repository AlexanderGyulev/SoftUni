size_of_field = int(input())

matrix = []

alice_pos = []

move_commands = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

total_tea_bags = 0

for index in range(size_of_field):
    current_list = input().split()
    matrix.append(current_list)
    if "A" in current_list:
        i = current_list.index("A")
        alice_pos = [index, i]
        matrix[alice_pos[0]][alice_pos[1]] = "*"

current_alice_pos = alice_pos

while True:
    if total_tea_bags >= 10:
        break
    current_command = input()
    i = current_alice_pos[0]
    y = current_alice_pos[1]
    current_alice_pos = [i + move_commands[current_command][0], y + move_commands[current_command][1]]
    if 0 <= current_alice_pos[0] < len(matrix) and 0 <= current_alice_pos[1] < len(matrix):
        if matrix[current_alice_pos[0]][current_alice_pos[1]].isdigit():
            total_tea_bags += int(matrix[current_alice_pos[0]][current_alice_pos[1]])
            matrix[current_alice_pos[0]][current_alice_pos[1]] = "*"
        elif matrix[current_alice_pos[0]][current_alice_pos[1]] == "R":
            matrix[current_alice_pos[0]][current_alice_pos[1]] = "*"
            break
        else:
            matrix[current_alice_pos[0]][current_alice_pos[1]] = "*"
    else:
        break

if total_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for index in range(len(matrix)):
    print(f"{' '.join(str(x) for x in matrix[index])}")
