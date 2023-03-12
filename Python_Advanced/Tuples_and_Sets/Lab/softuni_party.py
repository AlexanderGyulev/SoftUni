number_of_guests = int(input())

reservation_set = set()
arrived_guests = set()

for _ in range(number_of_guests):
    current_reservation = input()
    reservation_set.add(current_reservation)

while True:
    current_command = input()
    if current_command == "END":
        break
    arrived_guests.add(current_command)

missing_list = sorted(list(reservation_set.difference(arrived_guests)))

missing_guests = len(missing_list)
print(missing_guests)

if len(reservation_set) != 0:
    for element in missing_list:
        print(element)
