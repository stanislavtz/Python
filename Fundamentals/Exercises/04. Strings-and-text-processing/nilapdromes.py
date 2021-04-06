string = input()

while string != 'end':
    border_lenght = 0
    for i in range(0, len(string) // 2):
        l = string[:i+1]
        r = string[-1-i:]
        if l == r:
            current_border_lenght = len(string[:i+1])
            if current_border_lenght > border_lenght:
                border_lenght = current_border_lenght

    border = string[:border_lenght]
    core = string[border_lenght:-border_lenght]
    if border and core:
        print(f"{core}{border}{core}")
    
    string = input()