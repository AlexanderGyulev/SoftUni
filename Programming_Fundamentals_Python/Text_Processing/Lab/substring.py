first_input = input()
second_input = input()

while first_input in second_input:
    second_input = second_input.replace(first_input, "")
print(second_input)
