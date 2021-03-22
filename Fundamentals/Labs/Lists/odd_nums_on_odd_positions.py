li = list(map(lambda x: int(x), input().split()))

for i in range(1, len(li), 2):
    if li[i] % 2 != 0:
        print(f'Index {i} -> {li[i]}')