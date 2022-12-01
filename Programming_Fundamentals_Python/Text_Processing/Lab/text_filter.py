banned_words = input().split(", ")
text = input()

for words in banned_words:
    while words in text:
        text = text.replace(words, "*" * len(words))
print(text)