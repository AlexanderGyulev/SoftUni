def electron_operations(total_electrons):
    index = 1
    list_of_electrons = []
    while True:
        current_electron = 2 * (index ** 2)
        if total_electrons - current_electron >= 0:
            total_electrons -= current_electron
            list_of_electrons.append(current_electron)
        else:
            list_of_electrons.append(total_electrons)
            break
        index += 1
    return list_of_electrons


number_of_electrons = int(input())
result = electron_operations(number_of_electrons)
print(result)
