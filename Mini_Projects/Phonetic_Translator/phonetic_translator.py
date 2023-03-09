sentence_for_transformation = input()

letters_dictionary = {"a": "Alpha", "b": "Beta", "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot", "g": "Golf",
                      "h": "Hotel", "i": "India", "j": "Juliett", "k": "Kilo", "l": "Lima", "m": "Mike",
                      "n": "November", "o": "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra","t": "Tango",
                      "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "X-Ray", "y": "Yankee", "z": "Zulu"}

final_text = ""

for letters in sentence_for_transformation:
    if letters.isalpha():
        current_word = letters_dictionary[letters.lower()]
        final_text = final_text + current_word + " "
    else:
        final_text = final_text + letters + " "

print(final_text)
