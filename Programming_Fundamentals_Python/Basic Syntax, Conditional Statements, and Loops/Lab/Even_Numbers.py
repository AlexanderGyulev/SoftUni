total_numbers = int(input())

for i in range(0, total_numbers):
    get_number = int(input())
    if get_number % 2 != 0:
        print(f'{get_number} is odd!')
        break
else:
    print("All numbers are even.")