sequence = input().split(" ")
occurrences_dict = {}
for word in sequence:
    word = word.lower()
    if word not in occurrences_dict:
        occurrences_dict[word.lower()] = 0
    occurrences_dict[word.lower()] += 1

for key, value in occurrences_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
