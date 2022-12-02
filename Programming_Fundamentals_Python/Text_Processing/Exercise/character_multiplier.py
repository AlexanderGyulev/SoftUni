str1, str2 = input().split(" ")

total_sum = 0

length_str1 = len(str1)
length_str2 = len(str2)

if length_str1 == length_str2:
    for items in range(len(str1)):
        current_sum = ord(str1[items]) * int(ord(str2[items]))
        total_sum += current_sum
elif length_str1 > length_str2:
    for items in range(len(str2)):
        current_sum = ord(str1[items]) * int(ord(str2[items]))
        total_sum += current_sum
    for elements in range(length_str2, length_str1):
        current_sum = ord(str1[elements])
        total_sum += current_sum
elif length_str2 > length_str1:
    for items in range(len(str1)):
        current_sum = ord(str1[items]) * int(ord(str2[items]))
        total_sum += current_sum
    for elements in range(length_str1, length_str2):
        current_sum = ord(str2[elements])
        total_sum += current_sum
print(total_sum)
