nums = list(map(int, input().split()))
searched_value = int(input())

if nums.count(searched_value) > 0:
    print('yes')
else:
    print('no')
