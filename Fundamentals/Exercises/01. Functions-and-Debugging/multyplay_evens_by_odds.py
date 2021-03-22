def sum_odds(value):
    sum = 0
    for v in value:
        if int(v) % 2 == 1:
            sum += int(v)
    return sum

def sum_evens(value):
    sum = 0
    for v in value:
        if int(v) % 2 == 0:
            sum += int(v)
    return sum

def multyplay_odds_evens():
    val = str(abs(int(input())))
    return sum_evens(val) * sum_odds(val)


print(multyplay_odds_evens())
