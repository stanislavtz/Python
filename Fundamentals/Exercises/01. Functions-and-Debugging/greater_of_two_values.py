def convert_to_int(a, b):
    a = int(a)
    b = int(b)
    return a, b

def convert_to_upper(a, b):
    a = a.upper()
    b = b.upper()
    return a, b

def get_max(t, a, b):
    if t == 'int':
        a, b = convert_to_int(a, b)
    elif t == 'char':
        a, b = convert_to_upper(a, b)
    arr = [a, b]
    return f'Result: {max(arr)}'


value_type = input('Input type: ')
v_1 = input('Input first value: ')
v_2 = input('Input second value: ')

print(get_max(value_type, v_1, v_2))