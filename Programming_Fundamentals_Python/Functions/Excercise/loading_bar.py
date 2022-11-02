def loading_bar_operations(num):
    num = int(num / 10)
    final_string = ""
    for items in range(num):
        final_string += "%"
    for elements in range(num, 10):
        final_string += "."
    return final_string


integer_number = int(input())
if integer_number < 100:
    print(f"{integer_number}% [{loading_bar_operations(integer_number)}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f'[{loading_bar_operations(integer_number)}]')
