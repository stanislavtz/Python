result = {}
data = input()
while data != 'end':
    key, value = data.split(' -> ')[0], data.split(' -> ')[1]

    temp = value.split(', ')
    
    if len(value.split(', ')) > 1 or value.isdigit():
        if not key in result:
            result[key] = value
        else:
            result[key] += f", {value}"
    else:
        if value in result:
            result[key] = result[value]

    data = input()

for k, v in result.items():
    print(f"{k} === {v}")