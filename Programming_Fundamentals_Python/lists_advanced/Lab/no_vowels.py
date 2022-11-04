def vowel_removal(text):
    vowels_list = ["a", "o", "u", "e", "i"]
    no_vowels = "".join(x for x in text if x.lower() not in vowels_list)
    return no_vowels


text_string = input()
print(vowel_removal(text_string))
