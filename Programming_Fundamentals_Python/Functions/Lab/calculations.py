user_operator = input()
first_number = int(input())
second_number = int(input())


def calculation_function(a, b, operator):
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a / b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    result = int(result)
    return result


print(calculation_function(first_number, second_number, user_operator))
