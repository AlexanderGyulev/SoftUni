input_string = sorted(list(input()))

input_set = set()

for element in input_string:
    if element not in input_set:
        counter = input_string.count(element)
        print(f"{element}: {counter} time/s")
        input_set.add(element)
    else:
        continue
