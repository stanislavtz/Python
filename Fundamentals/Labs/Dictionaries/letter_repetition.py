string = input()
d = {}

for s in string:
    if not s in d:
        d[s] = 0
    d[s] += 1

for k, v in d.items():
    print(f"{k} -> {v}")