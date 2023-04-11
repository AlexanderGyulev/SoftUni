def math_operations(*args, **kwargs):
    index = 0
    for element in args:
        if index == 4:
            index = 0
        if index == 0:
            kwargs['a'] += element
        elif index == 1:
            kwargs['s'] -= element
        elif index == 2:
            if element != 0:
                kwargs['d'] /= element
        elif index == 3:
            kwargs['m'] *= element
        index += 1
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{k}: {v:.1f}" for k, v in kwargs)


