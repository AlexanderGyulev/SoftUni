nums = tuple(map(float, input().split()))

nums_dict = {}

for elements in nums:
    if elements not in nums_dict.keys():
        nums_dict[elements] = nums.count(elements)

for keys in nums_dict.keys():
    print(f"{keys} - {nums_dict[keys]} times")
