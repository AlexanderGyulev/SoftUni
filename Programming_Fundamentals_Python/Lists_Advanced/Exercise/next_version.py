def versions(current_version):
    list_of_numbers = list(map(int, current_version))
    a = list_of_numbers[0]
    b = list_of_numbers[1]
    c = list_of_numbers[2]

    if c == 9:
        b += 1
        c = 0
    else:
        c += 1
    if b > 9:
        a += 1
        b = 0
    return a, b, c


version_string = input().split(".")
result = versions(version_string)
print(f"{result[0]}.{result[1]}.{result[2]}")
