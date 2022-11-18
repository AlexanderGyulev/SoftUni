from math import floor
group_size = int(input())
days_of_adventure = int(input())

total_coins = 0

for days in range(1, days_of_adventure + 1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    total_coins += 50 - (group_size * 2)
    if days % 3 == 0:
        total_coins -= 3 * group_size
    if days % 5 == 0:
        total_coins += 20 * group_size
        if days % 3 == 0:
            total_coins -= 2 * group_size

coins_per_companion = total_coins / group_size
coins_per_companion = floor(coins_per_companion)

print(f"{group_size} companions received {coins_per_companion} coins each.")