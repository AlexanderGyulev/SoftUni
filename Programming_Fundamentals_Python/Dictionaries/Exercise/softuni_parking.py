total_registrations = int(input())
registrations_dictionary = {}

for _ in range(total_registrations):
    command = input().split(" ")
    if command[0] == "register":
        username = command[1]
        license_plate = command[2]
        if username in registrations_dictionary.keys():
            old_license = registrations_dictionary[username]
            print(f"ERROR: already registered with plate number {old_license}")
        else:
            registrations_dictionary[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        username = command[1]
        if username not in registrations_dictionary.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registrations_dictionary[username]
            print(f"{username} unregistered successfully")

for keys, values in registrations_dictionary.items():
    print(f"{keys} => {values}")
