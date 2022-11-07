def to_do():
    to_do_list = ["will be deleted"] * 10
    while True:
        current_command = input().split("-")
        if current_command[0] == "End":
            break
        priority = int(current_command[0])
        task = current_command[1]
        to_do_list.insert(priority, task)
    final_result = [element for element in to_do_list if element != "will be deleted"]
    return final_result


print(to_do())
