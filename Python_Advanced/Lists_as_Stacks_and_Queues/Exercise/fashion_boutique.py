from collections import deque

sequence_of_clothes = deque(int(x) for x in input().split(" "))
rack_capacity = int(input())

total_racks = 1

while len(sequence_of_clothes) > 0:
    current_rack_total = 0
    for items in sequence_of_clothes.copy():
        if current_rack_total + items <= rack_capacity:
            current_rack_total += items
            sequence_of_clothes.pop()
        else:
            total_racks += 1
            current_rack_total = 0
            current_rack_total += items
            sequence_of_clothes.pop()

print(total_racks)
