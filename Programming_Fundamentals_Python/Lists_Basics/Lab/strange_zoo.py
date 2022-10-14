list1 = []

for i in range(3):
    data = input()
    list1.append(data)

list1[0], list1[2] = list1[2], list1[0]
print(list1)