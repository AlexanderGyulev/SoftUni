force_side_dictionary = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    user_flag = False
    if " | " in command:
        command = command.split(" | ")
        # input would be "{force_side} | {force_user}"
        side = command[0]
        user = command[1]
        if side not in force_side_dictionary.keys():
            force_side_dictionary[side] = list()
        for items in force_side_dictionary.values():
            if user in items:
                user_flag = True
        if not user_flag:
            force_side_dictionary[side].append(user)
    elif " -> " in command:
        command = command.split(" -> ")
        # input would be "{force_user} -> {force_side}"
        side = command[1]
        user = command[0]
        for keys,values in force_side_dictionary.items():
            if user in values:
                force_side_dictionary[keys].remove(user)
        if side not in force_side_dictionary.keys():
            force_side_dictionary[side] = list()
        force_side_dictionary[side].append(user)
        print(f'{user} joins the {side} side!')

for keys, values in force_side_dictionary.items():
    if len(values) == 0:
        continue
    else:
        print(f"Side: {keys}, Members: {len(values)}")
        for items in values:
            print(f"! {items}")
