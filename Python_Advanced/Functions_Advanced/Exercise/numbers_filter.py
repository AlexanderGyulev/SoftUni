def even_odd_filter(**kwargs):
    final_dictionary = {}
    for key, values in kwargs.items():
        final_dictionary[key] = []
        if key == "even":
            for element in values:
                if element % 2 == 0:
                    final_dictionary[key].append(element)
        elif key == "odd":
            for element in values:
                if element % 2 != 0:
                    final_dictionary[key].append(element)
    return dict(sorted(final_dictionary.items(), key=lambda x: len(x[1]), reverse=True))

