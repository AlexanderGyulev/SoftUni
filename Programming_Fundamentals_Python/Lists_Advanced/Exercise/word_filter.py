def even_text(sequence):
    filtered_list = [element for element in sequence if len(element) % 2 == 0]
    return filtered_list


text_input = input().split(" ")
result = even_text(text_input)
print("\n".join(result))
