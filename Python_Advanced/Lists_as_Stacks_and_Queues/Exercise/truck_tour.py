from collections import deque

number_of_petrol_pumps = int(input())

pump_deque = deque()

current_fuel = 0
index = 0

for elements in range(number_of_petrol_pumps):
    current_data = input().split()
    amount_of_petrol = int(current_data[0])
    next_petrol_pump = int(current_data[1])
    current_list = [int(amount_of_petrol), int(next_petrol_pump)]
    pump_deque.append(current_list)

pump_deque_copy = pump_deque.copy()

while pump_deque_copy:
    petrol, distance = pump_deque_copy.popleft()
    current_fuel += petrol
    if current_fuel < distance:
        pump_deque.rotate(-1)
        pump_deque_copy = pump_deque.copy()
        index += 1
        current_fuel = 0
    else:
        current_fuel -= distance

print(index)
