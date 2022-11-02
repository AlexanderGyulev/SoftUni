def factorial_operations(first, second):
    first_factorial = 1
    second_factorial = 1
    for items in range(first, 0, -1):
        first_factorial = first_factorial * items
    for elements in range(second, 0, -1):
        second_factorial = second_factorial * elements
    result = first_factorial / second_factorial
    return result


first_int = int(input())
second_int = int(input())
print(f"{factorial_operations(first_int, second_int):.2f}")
