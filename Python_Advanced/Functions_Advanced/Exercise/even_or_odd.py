def even_odd(*args):
    command = args[-1]
    list_of_values = []
    if command == "even":
        for num in range(len(args)-1):
            if args[num] % 2 == 0:
                list_of_values.append(args[num])
    elif command == "odd":
        for num in range(len(args) - 1):
            if args[num] % 2 != 0:
                list_of_values.append(args[num])
    return list_of_values
