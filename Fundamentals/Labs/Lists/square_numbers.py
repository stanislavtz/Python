import math

numbers = list(map(lambda x: int(x), input().split()))
temp = []

for num in numbers:
    if num <= 0:
        continue
    res = math.sqrt(num)
    if res % 1 == 0:
        temp.append(num)

sorted_nums = list(map(lambda x: str(x), sorted(temp, reverse=True)))
print(' '.join(sorted_nums))