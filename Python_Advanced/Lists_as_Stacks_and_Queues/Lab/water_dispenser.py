from collections import deque

water_quantity = int(input())
people_que = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        people_que.append(name)

while True:
    command = input()
    if command == "End":
        break
    elif "refill" in command:
        command = command.split(" ")
        refill_quantity = int(command[1])
        water_quantity += refill_quantity
    else:
        command = int(command)
        if water_quantity >= command:
            print(f'{people_que.popleft()} got water')
            water_quantity -= command
        else:
            print(f'{people_que.popleft()} must wait')

print(f'{water_quantity} liters left')
