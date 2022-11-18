def palindrome_check(sequence):
    list_results = []
    for item in sequence:
        if item == item[:: -1]:
            list_results.append(True)
        else:
            list_results.append(False)
    return list_results


sequence_of_integers = input().split(", ")
result = palindrome_check(sequence_of_integers)
print(*result, sep="\n")
