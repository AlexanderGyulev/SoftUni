n = int(input())

matrix = [list(map(int, input().split())) for x in range(n)]

coordinates_of_bombs = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
    (-1, 1),  # top right
    (-1, -1),  # top left
    (1, -1),  # bottom left
    (1, 1),  # bottom right
    (0, 0)  # current position
)

for row, col in coordinates_of_bombs:
    if matrix[row][col] <= 0:
        continue
    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for x in range(len(matrix)):
    print(f"{' '.join(str(x) for x in matrix[x])}")
