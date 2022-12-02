normal_text = input()

encrypted_text = ""

for elements in normal_text:
    current_element_ascii = ord(elements)
    new_element = chr(current_element_ascii + 3)
    encrypted_text += new_element

print(encrypted_text)
