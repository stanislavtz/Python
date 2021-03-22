def print_header(number):
    for i in range(1, number+1):
        print(i, end=' ')

def print_footer(number):
    for i in range(1, number):
        print(i, end=' ')
    
def print_triangle(num):
    for j in range(1, num+1):
        print_header(j)
        print()
    for j in reversed(range(1, num+1)):
        print_footer(j)
        print()


print_triangle(int(input()))