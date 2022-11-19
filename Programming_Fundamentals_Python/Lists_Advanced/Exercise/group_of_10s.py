def groups_operations(sequence):
    sequence = list(map(int, sequence))
    max_num = max(sequence)
    start_index = 0
    end_index = 10
    while True:
        current_list = []
        for numbers in sequence:
            if start_index < numbers <= end_index:
                current_list.append(numbers)
        if len(current_list) != 0:
            if max(current_list) < max_num:
                print(f"Group of {end_index}'s: {current_list}")
                start_index += 10
                end_index += 10
            elif max(current_list) == max_num:
                print(f"Group of {end_index}'s: {current_list}")
                break
        else:
            print(f"Group of {end_index}'s: {current_list}")
            start_index += 10
            end_index += 10
            continue


string_of_numbers = input().split(", ")
groups_operations(string_of_numbers)
