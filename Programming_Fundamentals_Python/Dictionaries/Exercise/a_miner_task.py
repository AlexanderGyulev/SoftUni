resource_dictionary = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resource_dictionary.keys():
        resource_dictionary[resource] = quantity
    else:
        resource_dictionary[resource] += quantity

for keys, values in resource_dictionary.items():
    print(f"{keys} -> {values}")
