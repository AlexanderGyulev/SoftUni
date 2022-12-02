input_string = input()

for index in range(len(input_string)):
    if input_string[index] == ":":
        print(f":{input_string[index + 1]}")
