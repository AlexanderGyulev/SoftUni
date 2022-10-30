first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_number(a, b, c):
    smallest_num = min(a, b, c)
    return smallest_num


print(smallest_number(first_number, second_number, third_number))
