number_of_names = int(input())

set_of_names = set()

for _ in range(number_of_names):
    current_name = input()
    set_of_names.add(current_name)

for elements in set_of_names:
    print(elements)
