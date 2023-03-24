sequence_of_elements = input().split("|")

final_list = []

for sub_string in sequence_of_elements[::-1]:
    final_list.extend(sub_string.split())

print(f"{' '.join(x for x in final_list)}")
