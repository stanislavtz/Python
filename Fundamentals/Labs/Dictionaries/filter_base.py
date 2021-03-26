ages_db = {}
salaries_db = {}
positions_db = {}

data = input()
while data != 'filter base':
    name = data.split(' -> ')[0]
    attr = data.split(' -> ')[1]

    if not attr.isalpha():
        if float(attr) % 1 == 0:
            ages_db[name] = attr
        else:
            salaries_db[name] = attr
    else:
        positions_db[name] = attr
        
    data = input()

criteria = input()

result_db = None
if criteria == 'Age':
    result_db = ages_db.copy()
elif criteria == 'Salary':
    result_db = salaries_db.copy()
else:
    result_db = positions_db.copy()
    

for k, v in result_db.items():
    print(f"{'Name'}: {k}\n{criteria}: {v}\n{'='*20}")