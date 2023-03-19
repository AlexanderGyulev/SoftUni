size_of_matrix = int(input())


def diagonal_square_matrix(size):
    final_sum = 0
    for element in range(size_of_matrix):
        current_element = list(map(int, input().split(" ")))
        final_sum += current_element[element]
    return final_sum


print(diagonal_square_matrix(size_of_matrix))
