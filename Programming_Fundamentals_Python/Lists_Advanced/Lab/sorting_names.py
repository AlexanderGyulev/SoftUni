def sorting(sequence):
    result = sorted(sequence, key=lambda x: (-len(x), x))
    return result


names = input().split(", ")
print(sorting(names))
