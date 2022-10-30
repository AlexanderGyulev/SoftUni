first_integer = int(input())
second_integer = int(input())
third_integer = int(input())


def sum_numbers():
    x = first_integer + second_integer
    return x


def subtract():
    y = sum_numbers() - third_integer
    return y


def add_and_subtract():
    sum_numbers()
    subtract()
    return subtract()


print(add_and_subtract())
