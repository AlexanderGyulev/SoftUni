factor = int(input())
count = int(input())

multiples_list = []

for nums in range(1, count+1):
    current_number = factor * nums
    multiples_list.append(current_number)

print(multiples_list)