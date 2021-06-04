nums = sorted(list(map(lambda x: int(x), input().split())))
numbers = []

for num in nums:
    if numbers.count(num) == 0:
        numbers.append(num)

for num in numbers:
    print(f"{num} -> {nums.count(num)}")
    
    
 print('test')   