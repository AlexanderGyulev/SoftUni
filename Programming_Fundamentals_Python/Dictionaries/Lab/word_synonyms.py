dictionary_of_words = {}
word_count = int(input())

for words in range(word_count):
    current_key = input()
    current_value = input()
    if current_key not in dictionary_of_words.keys():
        dictionary_of_words[current_key] = [current_value]
    else:
        dictionary_of_words[current_key] += [current_value]

for items in dictionary_of_words.keys():
    elements = dictionary_of_words[items]
    print(f"{items} - {', '.join(elements)}")
