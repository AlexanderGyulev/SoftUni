first_character = int(input())
last_character = int(input())

for i in range(first_character, last_character + 1):
    print(chr(i), end=' ')
