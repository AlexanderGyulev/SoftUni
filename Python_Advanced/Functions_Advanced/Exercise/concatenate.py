def concatenate(*args, **kwargs):
    words = [x for x in args]
    final_string = ''
    for mini_string in words:
        final_string += mini_string
    for key,value in kwargs.items():
        if key in final_string:
            final_string = final_string.replace(key, value)
    return final_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
