def palindrome_checker(sequence, word):
    list_of_strings = sequence
    list_of_palindromes = []
    for items in list_of_strings:
        if items == items[:: -1]:
            list_of_palindromes.append(items)
    palindrome_counter = list_of_strings.count(word)
    return list_of_palindromes, palindrome_counter


sequence_of_strings = input().split(" ")
palindrome = input()
result = palindrome_checker(sequence_of_strings, palindrome)
all_palindromes = result[0]
counter = result[1]
print(all_palindromes)
print(f"Found palindrome {counter} times")
