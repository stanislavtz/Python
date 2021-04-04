data = input()
obj = {}

for i in range(len(data)):
    letter = data[i]
    if not letter in obj:
        obj[letter] = []
    obj[letter].append(i)
    
for k, v in obj.items():
    print(f"{k}:{'/'.join(map(str, v))}")