store = {}

data = input()
while data != 'exam time':
    command = data.split()[0]
    product = data.split()[1]

    if command == 'stock':
        qtty = int(data.split()[2])
        if not product in store.keys():
            store[product] = 0
        store[product] += qtty

    elif command == 'buy':
        qtty = int(data.split()[2])

        if not product in store.keys():
            print(f"{product} doesn't exist")
            data = input()
            continue

        if store[product] == 0:
            print(f"{product} out of stock")
            data = input()
            continue
        
        if qtty > store[product]:
            store[product] = 0
        else:
            store[product] -= qtty

    data = input()

for k,v in store.items():
    if v > 0:
        print(f"{k} -> {v}")
        