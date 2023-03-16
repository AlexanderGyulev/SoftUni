from collections import deque

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

toys_dict = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials and magic_levels:
    curr_material = materials.pop()
    curr_level = magic_levels.popleft()
    total_magic_lvl = curr_material * curr_level

    if total_magic_lvl < 0:
        materials.append(curr_material + curr_level)
        continue
    elif total_magic_lvl not in [150, 250, 300, 400] and total_magic_lvl > 0:
        materials.append(curr_material + 15)
        continue
    elif curr_level == 0 and curr_material == 0:
        continue
    elif curr_level == 0:
        materials.append(curr_material)
        continue
    elif curr_material == 0:
        magic_levels.appendleft(curr_level)
        continue
    if total_magic_lvl == 150:
        toys_dict["Doll"] += 1
    elif total_magic_lvl == 250:
        toys_dict["Wooden train"] += 1
    elif total_magic_lvl == 300:
        toys_dict["Teddy bear"] += 1
    elif total_magic_lvl == 400:
        toys_dict["Bicycle"] += 1

if (toys_dict["Doll"] >= 1 and toys_dict["Wooden train"] >= 1) \
        or (toys_dict["Teddy bear"] >= 1 and toys_dict["Bicycle"] >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for i in sorted(toys_dict):
    if toys_dict[i] >= 1:
        print(f"{i}: {toys_dict[i]}")
