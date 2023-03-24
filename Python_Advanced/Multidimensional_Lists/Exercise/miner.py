import sys

n = int(input())

matrix = []

total_coal = 0
total_coal_gathered = 0
start_pos = [0, 0]

commands = list(input().split())

for i in range(n):
    curr_list = input().split(" ")
    for el in curr_list:
        if el == "c":
            total_coal += 1
    if "s" in curr_list:
        start_pos = curr_list.index("s")
        start_pos = [i, start_pos]
    matrix.append(curr_list)

curr_position = start_pos

for curr_command in commands:
    if curr_command == "up":
        x = int(curr_position[0] - 1)
        y = int(curr_position[1])
        if x not in range(len(matrix)) or y not in range(len(matrix[x])):
            continue
        curr_position = [x, y]
    elif curr_command == "down":
        x = int(curr_position[0] + 1)
        y = int(curr_position[1])
        if x not in range(len(matrix)) or y not in range(len(matrix[x])):
            continue
        curr_position = [x, y]
    elif curr_command == "left":
        x = int(curr_position[0])
        y = int(curr_position[1] - 1)
        if x not in range(len(matrix)) or y not in range(len(matrix[x])):
            continue
        curr_position = [x, y]
    else:
        x = int(curr_position[0])
        y = int(curr_position[1] + 1)
        if x not in range(len(matrix)) or y not in range(len(matrix[x])):
            continue
        curr_position = [x, y]

    if matrix[x][y] == "c":
        total_coal_gathered += 1
        matrix[x][y] = "*"

    if matrix[x][y] == "e":
        print(f"Game over! ({', '.join(str(x) for x in curr_position)})")
        sys.exit()
    elif total_coal == total_coal_gathered:
        print(f"You collected all coal! ({', '.join(str(x) for x in curr_position)})")
        sys.exit()

print(f"{total_coal - total_coal_gathered} pieces of coal left. ({', '.join(str(x) for x in curr_position)})")
