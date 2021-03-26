key, value = input(), input()
n = int(input())
result = {}

for i in range(n):
    data = input()
    k = data.split(' => ')[0]
    values = data.split(' => ')[1].split(';')

    isKey = key in k
    isValue = value in data.split(' => ')[1]

    if isKey == True:
        if not k in result:
            result[k] = []

        if isValue == True:
            result[k] += list(filter(lambda v: value in v, values))

for k, v in result.items():
    print(f"{k}:")
    if len(v) > 0:
        print('\n'.join(map(lambda x: f"-{x}", v)))