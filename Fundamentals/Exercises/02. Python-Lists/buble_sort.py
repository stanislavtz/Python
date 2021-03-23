nums = list(map(int, input().split()))
i = -1
while i < len(nums)-2:
    i += 1
    if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        i = -1
        
print(' '.join(map(str,nums)))
