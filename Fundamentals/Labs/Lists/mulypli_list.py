def multyply(li, p):
    return ' '.join(list(map(lambda x: str(x*p), li)))

li, p = list(map(lambda x: int(x), input().split())), int(input())
print(multyply(li, p))