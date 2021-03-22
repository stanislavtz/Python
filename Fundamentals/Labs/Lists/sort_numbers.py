numbers = list(map(lambda x: int(x), input().split()))

sorted_nums = list(map(lambda x: str(x), sorted(numbers)))
print(' <= '.join(sorted_nums))