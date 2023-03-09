nums = tuple(map(float, input().split()))

nums_dict = {}

for elements in nums:
    if elements not in nums_dict.keys():
        nums_dict[elements] = nums.count(elements)

for keys, values in nums_dict.items():
    print(f"{keys} - {values} times")
