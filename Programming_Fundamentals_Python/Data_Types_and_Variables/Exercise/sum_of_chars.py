total_letters = int(input())


total_sum = 0

for i in range(total_letters):
    get_digit = input()
    total_sum += ord(get_digit)

print(f"The sum equals: {total_sum}")