award = ""
item_flag = False
items_dictionary = {}

while not item_flag:
    sequence_of_items = input().split(" ")
    for items in range(1, len(sequence_of_items) + 1, 2):
        if item_flag:
            break
        item = sequence_of_items[items].lower()
        amount = int(sequence_of_items[items - 1])
        if item not in items_dictionary:
            items_dictionary[item] = 0
        items_dictionary[item] += int(amount)

        for key, value in items_dictionary.items():
            if value >= 250 and key in ["shards", "fragments", "motes"]:
                if key == "shards":
                    award = "Shadowmourne"
                elif key == "fragments":
                    award = "Valanyr"
                elif key == "motes":
                    award = "Dragonwrath"
                items_dictionary[key] = int(value - 250)
                item_flag = True

print(f'{award} obtained!')
if "shards" in items_dictionary:
    print(f"shards: {items_dictionary['shards']}")
else:
    print(f"shards: 0")
if "fragments" in items_dictionary:
    print(f"fragments: {items_dictionary['fragments']}")
else:
    print("fragments: 0")
if "motes" in items_dictionary:
    print(f"motes: {items_dictionary['motes']}")
else:
    print("motes: 0")

for keys, values in items_dictionary.items():
    if keys != "shards" and keys != "fragments" and keys != "motes":
        print(f"{keys}: {values}")
