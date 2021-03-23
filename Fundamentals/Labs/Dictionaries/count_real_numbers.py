nums = list(map(float, input().split()))
unsorted_nums = {}

for num in nums:
    if num not in unsorted_nums.keys():
        unsorted_nums[num] = 0
    unsorted_nums[num] += 1

sorted_nums = sorted(unsorted_nums.items(), key= lambda x: x[0], reverse=False)

for k, v in sorted_nums:
    print(f'{k} -> {v} times')        