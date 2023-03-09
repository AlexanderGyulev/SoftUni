nums = tuple(map(float, input().split()))

nums_dict = {}

for elements in nums:
    if elements not in nums_dict.keys():
        nums_dict[elements] = 1
    else:
        nums_dict[elements] += 1

for keys in nums_dict.keys():
    print(f"{keys} - {nums_dict[keys]} times")
