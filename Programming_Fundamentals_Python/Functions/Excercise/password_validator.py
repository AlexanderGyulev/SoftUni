def password_checker(passcode):
    digit_count = 0
    problems = []
    if 6 > len(passcode) or len(passcode) > 10:
        problems.append("Password must be between 6 and 10 characters")
    if not passcode.isalnum():
        problems.append("Password must consist only of letters and digits")
    for elements in passcode:
        if elements.isdigit():
            digit_count += 1
    if digit_count < 2:
        problems.append("Password must have at least 2 digits")
    return problems


def empty_checker(random_list):
    if len(random_list) == 0:
        random_list.append("Password is valid")
    return random_list


password_string = input()
checks = password_checker(password_string)
result = empty_checker(checks)
print(*result, sep="\n")
