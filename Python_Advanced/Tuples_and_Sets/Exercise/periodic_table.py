count_of_input_lines = int(input())

final_set = set()

for _ in range(count_of_input_lines):
    current_input = input().split(" ")
    for item in current_input:
        final_set.add(item)

print(*final_set, sep="\n")
