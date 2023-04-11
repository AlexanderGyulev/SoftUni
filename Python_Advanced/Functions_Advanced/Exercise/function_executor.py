def func_executor(*args):
    result = []
    for func, arguments in args:
        func_res = func(*arguments)
        result.append(f"{func.__name__} - {func_res}")
    return '\n'.join(result)
