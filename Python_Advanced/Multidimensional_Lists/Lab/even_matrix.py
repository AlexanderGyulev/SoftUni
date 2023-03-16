rows = int(input())

final_list = []

for rows_index in range(rows):
    curr_list = [x for x in map(int, input().split(", ")) if x % 2 == 0]
    final_list.append(curr_list)

print(final_list)
