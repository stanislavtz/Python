nums = list(map(float, input().split()))
result = {}

for num in nums:
    if num not in result.keys():
        result[num] = 0
    result[num] += 1

sorted_result = (sorted(result.items(), key= lambda x: x[0], reverse=False))

for k, v in sorted_result:
    print(f'{k} -> {v} times')        