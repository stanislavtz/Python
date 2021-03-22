numbers = list(filter(lambda x: int(x) >= 0, input().split()))
if len(numbers) > 0:
    print(' '.join(list(reversed(list(map(lambda x: str(x), numbers))))))
else:
    print('empty')