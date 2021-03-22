li = input().split(' ')
li.insert(0, li.pop(-1))
print(' '.join(li))