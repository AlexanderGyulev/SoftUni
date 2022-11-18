number_of_rooms = int(input())

free_chairs = 0
problems_list = []

for rooms in range(1, number_of_rooms + 1):
    current_room = input().split(" ")
    if len(current_room[0]) >= int(current_room[1]):
        difference = len(current_room[0]) - int(current_room[1])
        free_chairs += difference
    else:
        difference = int(current_room[1]) - len(current_room[0])
        problems_list.append(f"{difference} more chairs needed in room {rooms}")
if len(problems_list) == 0:
    print(f"Game On, {free_chairs} free chairs left")
else:
    print(*problems_list, sep="\n")
