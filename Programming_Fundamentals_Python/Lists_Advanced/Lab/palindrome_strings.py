def palindrome_checker(sequence):
    list_of_strings = sequence
    list_of_palindromes = []
    for items in list_of_strings:
        if items == items[:: -1]:
            list_of_palindromes.append(items)
    return list_of_palindromes


sequence_of_strings = input().split(" ")
palindrome = input()
result = palindrome_checker(sequence_of_strings)
counter = sequence_of_strings.count(palindrome)
print(result)
print(f"Found palindrome {counter} times")
