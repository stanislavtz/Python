state = input()

while state != 'collapse':
    fiction = input()

    while len(fiction) >= 1:
        if fiction in state:
            state = state.replace(fiction, '')
        fiction = fiction[1:-1]

    if len(state) > 0: 
        print(state.strip())
    else:
        print('(void)')

    state = input()