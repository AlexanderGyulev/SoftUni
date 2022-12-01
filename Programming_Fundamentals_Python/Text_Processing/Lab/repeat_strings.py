sequence_of_strings = input().split(" ")
for elements in sequence_of_strings:
    print(elements * len(elements),end="")