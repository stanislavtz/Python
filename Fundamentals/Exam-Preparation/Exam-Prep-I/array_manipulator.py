def exchange_positions(array, index):
    if index < 0 or index >= len(array):
        print('Invalid index')
    else:
        array = array[index+1:] + array[:index+1]

    return array


def max_number_index(array, result):
    enum_list = list(filter(lambda t: t[1]%2==result, list(enumerate(array))))
    if len(enum_list) == 0:
        return 'No matches'
    else:
        sorted_nums = list(sorted(enum_list, key=lambda t: (t[1], t[0])))
        max_index = sorted_nums[-1][0]
        return max_index


def min_number_index(array, result):
    enum_list = list(filter(lambda t: t[1]%2==result, list(enumerate(array))))
    if len(enum_list) == 0:
        return 'No matches'
    else:
        sorted_nums = list(sorted(enum_list, key=lambda t: (-t[1], t[0]))) 
        index = sorted_nums[-1][0]
        return index


def first_counted_nums(array, result):
    num_list = list(filter(lambda x: x%2==result, array))
    if len(num_list) == 0:
        return []
    elif count > len(num_list):
        return [] + num_list
    else:
        return num_list[:count]


def last_counted_nums(array, result):
    num_list = list(filter(lambda x: x%2==result, array))
    if len(num_list) == 0:
        return []
    elif count > len(num_list):
        return [] + num_list
    else:
        return num_list[-count:]


array = list(map(int, input().split()))
command_line = input()
result = None

while command_line != 'end':
    command_line = command_line.split()
    command = command_line[0]

    if command == 'exchange':
        index = int(command_line[1])
        array = exchange_positions(array, index)
    elif command == 'max':
        o_e = command_line[1]
        if o_e == 'odd':
            print(max_number_index(array, 1))
        elif o_e == 'even':
            print(max_number_index(array, 0))
    elif command == 'min':
        o_e = command_line[1]
        if o_e == 'odd':
            print(min_number_index(array, 1))
        elif o_e == 'even':
            print(min_number_index(array, 0))
    elif command == 'first':
        count = int(command_line[1])
        if count > len(array):
            print('Invalid count')
        else:
            o_e = command_line[2]
            if o_e == 'odd':
                print(first_counted_nums(array, 1))
            elif o_e == 'even':
                print(first_counted_nums(array, 0))
    elif command == 'last':
        count = int(command_line[1])
        if count > len(array):
            print('Invalid count')
        else:
            o_e = command_line[2]
            if o_e == 'odd':
                print(last_counted_nums(array, 1))
            elif o_e == 'even':
                print(last_counted_nums(array, 0))

    command_line = input()

print(f"[{', '.join(list(map(str,array)))}]")