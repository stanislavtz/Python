class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def produce_sound(self):
        return self.sound

    sound = None


class Dog(Animal):
    sound = "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __init__(self, name, age, legs):
        Animal.__init__(self, name, age)
        self.legs = legs

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.legs}"


class Cat(Animal):
    sound = "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __init__(self, name, age, intellegance):
        Animal.__init__(self, name, age)
        self.intellegance = intellegance

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.intellegance}"


class Snake(Animal):
    sound = "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def __init__(self, name, age, cruelty):
        Animal.__init__(self, name, age)
        self.cruelty = cruelty

    def __str__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}"


def create_animal(kind, name, age, prop):
    if kind == 'Dog':
        return Dog(name, age, prop)
    elif kind == 'Cat':
        return Cat(name, age, prop)
    elif kind == 'Snake':
        return Snake(name, age, prop)


animals = {
    "Dog": [],
    "Cat": [],
    "Snake": []
}

command = input()
while command != "I'm your Huckleberry":
    if command.split()[0] != 'talk':
        kind = command.split()[0]
        name = command.split()[1]
        age = command.split()[2]
        prop = command.split()[3]

        animal = create_animal(kind, name, age, prop)
        animals[kind].append(animal)
    else:
        name = command.split()[1]
        animals_list = []

        for v in animals.values():
            animals_list.extend(v)

        searched_results = list(filter(lambda x: x.name == name, animals_list))
        animal = searched_results[0]
        
        print(animal.produce_sound())

    command = input()

for animal_list in animals.values():
    for animal in animal_list:
        print(animal)