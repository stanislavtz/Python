def swap_elements(data, i_1, i_2):
    if int(i_1) < len(data) and int(i_2) < len(data):
        data[int(i_1)], data[int(i_2)] = data[int(i_2)], data[int(i_1)]

data = list(map(int, input().split()))
command = input()
counter = 0
while command != 'end':
    if command.split()[0] == 'swap':
        _, index_1, index_2 = command.split()
        swap_elements(data, index_1, index_2)
        print(data)
        counter += 1
    elif command == 'enumerate_list':
        print(list(enumerate(data)))
        counter += 1
    elif command == 'max':
        print(max(data))
        counter += 1
    elif command == 'min':
        print(min(data))
        counter += 1
    elif command.split()[0] == 'get_divisible':
        divider = int(command.split()[2])
        print(list(filter(lambda n: n%divider==0, data)))
        counter += 1
    
    command = input()

print(counter)