phone_book = {}

entry = input()
while entry != 'Over':
    li = entry.split(' : ')
    
    if li[0].isdigit():
        phone_book[li[1]] = li[0]
    else:
        phone_book[li[0]] = li[1]

    entry = input()

sorted_book = sorted(phone_book.items(), key=lambda x: x[0])
for k,v in sorted_book:
    print(f"{k} -> {v}")