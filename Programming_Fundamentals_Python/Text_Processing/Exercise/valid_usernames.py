usernames_string = input().split(", ")
valid_usernames = []

for elements in usernames_string:
    valid_flag = True
    if 3 <= len(elements) <= 16:
        for items in elements:
            if (items.isalnum() or items == "_" or items == "-") and valid_flag:
                pass
            else:
                valid_flag = False
                break
        if valid_flag:
            valid_usernames.append(elements)

print(*valid_usernames, sep="\n")
