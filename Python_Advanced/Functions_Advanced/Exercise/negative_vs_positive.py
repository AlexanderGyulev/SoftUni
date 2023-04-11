def separation(sequence):
    positives_sum = 0
    negatives_sum = 0

    for num in sequence:
        if num < 0:
            negatives_sum += num
        elif num > 0:
            positives_sum += num
    return positives_sum, negatives_sum


sequence_of_numbers = map(int, input().split())
result = separation(sequence_of_numbers)

print(result[1])
print(result[0])

if abs(result[1]) > abs(result[0]):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
