def define_sign(num):
    if num < 0:
        return 'negative'
    elif num > 0:
        return 'positive' 
    
    return 'zero'


num = int(input())
result = define_sign(num)
print(f'The number {num} is {result}.')