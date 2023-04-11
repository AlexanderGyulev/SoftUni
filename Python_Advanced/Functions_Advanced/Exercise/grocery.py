def grocery_store(**products):
    sorted_items = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ""
    for item, quantity in sorted_items:
        result += f"{item}: {quantity}\n"
    return result
