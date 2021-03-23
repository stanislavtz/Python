nums, n = sorted(list(map(int, input().split())), reverse=True), int(input())
print(' '.join(list(map(str, nums[:n]))))