get_age = int(input())

drink_type = ''

if get_age <= 14:
    drink_type = "toddy"
elif get_age <= 18:
    drink_type = "coke"
elif get_age <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"

print(f'drink {drink_type}')