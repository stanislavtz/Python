inp = input()
res = {}
while inp != 'end':
    li = inp.split(' = ')

    if li[1] in res.keys():
        res[li[0]] = res[li[1]]
    elif li[1].isdigit():
        res[li[0]] = int(li[1])
    
    inp = input()

for k,v in res.items():
    print(f"{k} === {v}")