import re

class Person:
    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __str__(self):
        result = [f"Name of the person: {self.name}."]
        result.append(f"Age of the person: {self.age}.")
        result.append(f"Birthdate of the person: {self.birthday}.")
        return '\n'.join(result)



people = []
data = input()
while data != 'make migrations':
    pattern = r'(?<=name is )[A-Z][a-z]+ [A-Z][a-z]+(?=\.)'
    name = re.search(pattern, data)
    if not name:
        data = input()
        continue

    pattern = r'(?<=am )\d+(?= years)'
    age = re.search(pattern, data)
    if not age or int(age.group()) <= 9 or int(age.group()) >= 100:
        data = input()
        continue

    pattern = r'(?<=on )\d{2}-\d{2}-\d{4}(?=\.)'
    date =  re.search(pattern, data)
    if not date:
        data = input()
        continue

    person = Person(name.group(), age.group(), date.group())
    people.append(person)

    data = input()

if len(people) == 0:
    print('DB is empty')
else:
    for p in people:
        print(p)