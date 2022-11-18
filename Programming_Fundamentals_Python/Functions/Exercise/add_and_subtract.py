first_integer = int(input())
second_integer = int(input())
third_integer = int(input())


def sum_numbers(first, second):
    x = first + second
    return x


def subtract(sum, third):
    y = sum - third
    return y


def add_and_subtract(first, second, third):
    sum_nums = sum_numbers(first, second)
    subtract_sums = subtract(sum_nums, third)
    return subtract_sums


print(add_and_subtract(first_integer, second_integer, third_integer))
