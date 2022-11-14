def list_operations(elements):
    list_of_items = [x * 0 for x in range(elements)]
    commands = input().split(" ")
    while commands[0] != "End":
        if "add" in commands[0]:
            list_of_items[-1] += int(commands[1])
        elif "insert" in commands[0]:
            index = int(commands[1])
            ppl_to_add = int(commands[2])
            list_of_items[index] += ppl_to_add
        elif "leave" in commands[0]:
            ppl_to_remove = int(commands[2])
            index = int(commands[1])
            list_of_items[index] -= ppl_to_remove
        commands = input().split(" ")
    return list_of_items


number_of_items = int(input())
result = list_operations(number_of_items)
print(result)
