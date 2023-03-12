set_a_length, set_b_length = map(int, input().split())

set_a = set()
set_b = set()

for _ in range(set_a_length):
    current_number = int(input())
    set_a.add(current_number)

for _ in range(set_b_length):
    current_number = int(input())
    set_b.add(current_number)

set_c = set_a.intersection(set_b)

print(*set_c, sep="\n")
