string_of_integers = input().split(", ")
count_of_beggars = int(input())

money_list_ints = []
final_sums = []

starting_index = 0

for item in string_of_integers:
    item = int(item)
    money_list_ints.append(item)

while starting_index < count_of_beggars:
    current_sum = 0
    for current_index in range(starting_index, len(money_list_ints), count_of_beggars):
        current_sum += money_list_ints[current_index]
    final_sums.append(current_sum)
    starting_index += 1

print(final_sums)