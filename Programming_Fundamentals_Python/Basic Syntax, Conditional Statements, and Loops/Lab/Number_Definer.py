number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number < 1 and number != 0:
        print("small positive")
    elif number < 1000000:
        print("positive")
    else:
        print("large positive")
elif number < 0:
    if number > -1 and number != 0:
        print("small negative")
    elif number > -1000000:
        print("negative")
    else:
        print("large negative")
