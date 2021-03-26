key, value = input(), input()
n = int(input())
result = {}

for i in range(n):
    data = input()
    key_data = data.split(' => ')[0]
    values = data.split(' => ')[1].split(';')

    isKey = key in key_data
    if isKey == True:
        if not key_data in result:
            result[key_data] = []

        isValue = value in data.split(' => ')[1]
        if isValue == True:
            result[key_data] += list(filter(lambda v: value in v, values))

for k, v in result.items():
    print(f"{k}:")
    if len(v) > 0:
        print('\n'.join(map(lambda x: f"-{x}", v)))