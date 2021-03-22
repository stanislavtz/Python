name, age, town, salary = input(), int(input()), input(), float(input())
age_range, salary_range = 'elder', 'high'
arr = [f'Name: {name}', f'Age: {age}', f'Town: {town}', f'Salary: ${salary:.2f}']

if age < 18:
    age_range = 'teen'
elif age < 70:
    age_range = 'adult'

if salary < 500:
    salary_range = 'low'
elif salary < 2000:
    salary_range = 'medium'

arr.append(f'Age range: {age_range}')
arr.append(f'Salary range: {salary_range}')

for i in arr:
    print(i)