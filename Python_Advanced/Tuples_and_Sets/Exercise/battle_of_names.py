lines_of_names = int(input())

odd_set = set()
even_set = set()

for iteration in range(1, lines_of_names + 1):
    current_word = input()
    current_ascii_sum = 0
    for element in current_word:
        current_element = int(ord(element))
        current_ascii_sum += current_element
    final_el_sum = int(current_ascii_sum / iteration)
    if final_el_sum % 2 == 0:
        even_set.add(int(final_el_sum))
    else:
        odd_set.add(int(final_el_sum))

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")
