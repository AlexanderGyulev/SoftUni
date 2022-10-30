string_of_integers = input().split(" ")

integer_list = []
rounded_list = []


def to_list():
    for items in string_of_integers:
        integer_list.append(float(items))
    rounding()


def rounding():
    for elements in integer_list:
        rounded_list.append(int(round(elements)))
    print(rounded_list)


to_list()
