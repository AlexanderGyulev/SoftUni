number_of_symbols = int(input())

for first_letter in range(number_of_symbols):
    for second_letter in range(number_of_symbols):
        for third_letter in range(number_of_symbols):
            current_third_letter = chr(97)
            print(f'{chr(first_letter + 97)}{chr(second_letter + 97)}{chr(third_letter + 97)}')

