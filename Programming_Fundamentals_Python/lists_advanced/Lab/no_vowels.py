def vowel_removal(text):
    vowels_list = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "i"]
    no_vowels = "".join(x for x in text if x not in vowels_list)
    return no_vowels


text_string = input()
print(vowel_removal(text_string))
