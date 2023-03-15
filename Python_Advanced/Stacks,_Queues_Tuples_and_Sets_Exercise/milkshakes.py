from collections import deque

chocolate_values = deque(map(int, input().split(", ")))
milk_values = deque(map(int, input().split(", ")))

total_milkshakes = 0

while chocolate_values and milk_values and total_milkshakes != 5:
    if chocolate_values[-1] <= 0 and milk_values[0] <= 0:
        chocolate_values.pop()
        milk_values.popleft()
    elif chocolate_values[-1] <= 0:
        chocolate_values.pop()
    elif milk_values[0] <= 0:
        milk_values.pop()
    elif chocolate_values[-1] == milk_values[0]:
        chocolate_values.pop()
        milk_values.popleft()
        total_milkshakes += 1
    else:
        milk_values.rotate(-1)
        chocolate_values[-1] = chocolate_values[-1] - 5

if total_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate_values) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_values) or 'empty'}")
