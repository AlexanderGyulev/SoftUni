def odd_or_even(num):
    odds = 0
    evens = 0
    for element in num:
        element = int(element)
        if element % 2 == 0:
            evens += element
        else:
            odds += element
    return odds, evens


integer_number = input()
result = odd_or_even(integer_number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
