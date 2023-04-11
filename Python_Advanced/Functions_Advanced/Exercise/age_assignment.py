def age_assignment(*args, **kwargs):
    args = sorted(args)
    names_and_ages_dict = {}
    for name in args:
        names_and_ages_dict[name] = 0

    for key, value in kwargs.items():
        for element in names_and_ages_dict.keys():
            if key == element[0]:
                names_and_ages_dict[element] = value
    result = ""
    for key, value in names_and_ages_dict.items():
        result += f"{key} is {value} years old.\n"
    return result
