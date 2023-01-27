from collections import deque

quantity_of_food = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))

for current_order in orders.copy():
    if quantity_of_food >= current_order:
        quantity_of_food -= current_order
        orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print("Orders left:", end=" ")
    print(*orders, sep=" ")
