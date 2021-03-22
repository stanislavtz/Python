def calculate(a, b):
    return a*b/2

def readInput():
    a = float(input())
    b = float(input())
    return [a, b]


num_1, num_2 = readInput()
area = calculate(num_1, num_2)
print(f'{area:.12g}')
