total_numbers = int(input())

positives_list = []
negatives_list = []

negatives_sum = 0

for nums in range(total_numbers):
    current_number = int(input())
    if current_number > 0:
        positives_list.append(current_number)
    else:
        negatives_list.append(current_number)

total_positives = len(positives_list)
negatives_sum = sum(negatives_list)

print(positives_list)
print(negatives_list)
print(f'Count of positives: {total_positives}')
print(f'Sum of negatives: {negatives_sum}')