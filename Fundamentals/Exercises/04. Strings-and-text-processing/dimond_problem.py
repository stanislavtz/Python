string = input()
index_l = string.find('<')
index_m = string.find('>')
output = []

while index_l >= 0:
    if index_m <= 0: 
        break
    
    if index_l < index_m:
        substring = string[index_l:index_m+1]
        carats = sum(list(map(int, list(filter(lambda x: x.isdigit(), substring)))))
        output.append(f"Found {carats} carat diamond")
        string = string[index_m+1:]
    elif index_m > 0:
        string = string[index_m+1:]
    
    index_l = string.find('<')
    index_m = string.find('>')

if len(output) > 0:
    print('\n'.join(output))
else:
    print('Better luck next time')