inp_list = input().split()
nums = list(map(float, inp_list))

i= 0
while i < len(nums) - 1:
    if nums[i] == nums[i+1]:
        nums[i] += nums[i+1]
        nums.remove(nums[i+1])
        i = 0
        continue
    i += 1

print(' '.join(list(map(lambda x: str(f'{x:g}'), nums))))