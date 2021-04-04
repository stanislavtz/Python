o, l = {}, []
data = input()

while data != 'end':
    letter = data.split(':')[0]
    indexes = list(map(int, data.split(':')[1].split('/')))
    l.extend(indexes)
    if not letter in o:
        o[letter] = []
    o[letter].extend(indexes)
    data = input()

for letter, indexes in o.items():
    for index in indexes:
        l[index] = letter
        
print(''.join(l))