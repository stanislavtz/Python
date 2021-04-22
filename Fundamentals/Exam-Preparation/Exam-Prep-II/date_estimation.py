import datetime

today_date = datetime.date(2018, 8, 26)
date = list(map(int, input().split('-')))
date = datetime.date(date[0], date[1], date[2])

if date < today_date:
    print('Passed')
elif date == today_date:
    print('Today date')
else:
    days = date - today_date
    print(f'{ days.days + 1} days left')