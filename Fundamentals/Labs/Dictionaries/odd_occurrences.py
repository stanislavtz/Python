def fill_collection(data):
    col = {}
    for d in map(lambda x: x.lower(), data):
        if not d in col.keys():
            col[d] = 0
        col[d] += 1
    
    return col

def generate_result(col):
    res = []
    for k, v in col.items():
        if v % 2 == 0:
            continue
        res.append(k)
    
    return res


data = input().split()
collection = fill_collection(data)
result = generate_result(collection)

print(', '.join(result))