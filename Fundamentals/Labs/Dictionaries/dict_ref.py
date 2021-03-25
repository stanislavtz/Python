inp = input()
res = {}
while inp != 'end':
    a = inp.split(' = ')[0]
    b = inp.split(' = ')[1]

    if b in res:
        res[a] = res[b]
    elif b.isdigit():
        res[a] = int(b)
    
    inp = input()

for k,v in res.items():
    print(f"{k} === {v}")