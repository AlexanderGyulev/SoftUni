number_of_names = int(input())

username_set = set()

for _ in range(number_of_names):
    current_name = input()
    username_set.add(current_name)

print(*username_set, sep='\n')
