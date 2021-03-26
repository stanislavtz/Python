import math

regions = {}

data = input()
while data != 'Aggregate':
    region = data.split()[0]
    size = int(data.split()[1])
    
    if not region in regions:
        regions[region] = []

    if not size in regions[region]:
        regions[region].append(size)

    data = input()

for k, v in regions.items():
    avrg =  sum(v) - (sum(v) / len(v))
    print(f"{k} -> {', '.join(map(lambda x: str(x), v))} ({math.ceil(avrg)})")