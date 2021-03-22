li = list(map(lambda x: int(x), input().split()))
res = list(filter(lambda x: x % 2 != 0, li))
print(len(res))