banned_words = input().split(", ")
text = input()

for words in banned_words:
    text = text.replace(words, "*" * len(words))
print(text)