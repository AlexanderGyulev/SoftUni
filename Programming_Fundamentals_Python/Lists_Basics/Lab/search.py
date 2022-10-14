number_of_words = int(input())
filter_word = input()

words_list = []
filtered_list = []

for nums in range(number_of_words):
    current_word = input()
    words_list.append(current_word)

for i in range(len(words_list)):
    if filter_word in words_list[i]:
        filtered_list.append(words_list[i])

print(words_list)
print(filtered_list)