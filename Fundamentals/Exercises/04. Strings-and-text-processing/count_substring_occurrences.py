string, sub, counter = input().lower(), input().lower(), 0

while True:
    if not sub in string:
        break
    counter += 1
    index = string.index(sub)
    string = string[index+1:]
    
print(counter)