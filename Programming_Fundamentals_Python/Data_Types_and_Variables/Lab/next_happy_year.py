current_year = int(input())

happy_year_condition = False
next_happy_year = 0
numbers_list = []

while not happy_year_condition:
    current_year = int(current_year) + 1
    current_year = str(current_year)
    if "1" in current_year:
        if 1 not in numbers_list:
            numbers_list.append(1)
    if "2" in current_year:
        if 2 not in numbers_list:
            numbers_list.append(2)
    if "3" in current_year:
        if 3 not in numbers_list:
            numbers_list.append(3)
    if "4" in current_year:
        if 4 not in numbers_list:
            numbers_list.append(4)
    if "5" in current_year:
        if 5 not in numbers_list:
            numbers_list.append(5)
    if "6" in current_year:
        if 6 not in numbers_list:
            numbers_list.append(6)
    if "7" in current_year:
        if 7 not in numbers_list:
            numbers_list.append(7)
    if "8" in current_year:
        if 8 not in numbers_list:
            numbers_list.append(8)
    if "9" in current_year:
        if 9 not in numbers_list:
            numbers_list.append(9)
    if "0" in current_year:
        if 0 not in numbers_list:
            numbers_list.append(0)
    if len(numbers_list) == len(current_year):
        happy_year_condition = True
        next_happy_year = current_year
    else:
        numbers_list = []

print(next_happy_year)


