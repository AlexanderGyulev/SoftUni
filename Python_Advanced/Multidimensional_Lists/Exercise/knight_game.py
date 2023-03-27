size_of_board = int(input())
matrix = [list(input()) for _ in range(size_of_board)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size_of_board):
        for col in range(size_of_board):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size_of_board and 0 <= pos_col < size_of_board:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
