from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def produce_sound(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, legs):
        Animal.__init__(self, name, age)
        self.legs = legs

    def produce_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.legs}"


class Cat(Animal):
    def __init__(self, name, age, intellegance):
        Animal.__init__(self, name, age)
        self.intellegance = intellegance

    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.intellegance}"


class Snake(Animal):
    def __init__(self, name, age, cruelty):
        Animal.__init__(self, name, age)
        self.cruelty = cruelty

    def produce_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def __str__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}"


def create_animal(kind, name, age, prop):
    if kind == 'Dog':
        return Dog(name, age, prop)
    elif kind == 'Cat':
        return Cat(name, age, prop)
    elif kind == 'Snake':
        return Snake(name, age, prop)


animals = []

command = input()
while command != "I'm your Huckleberry":
    if command.split()[0] != 'talk':
        kind, name, age, prop = command.split()
        animal = create_animal(kind, name, age, prop)

        animals.append(animal)
    else:
        name = command.split()[1]
        searched_results = list(filter(lambda x: x.name == name, animals))
        animal = searched_results[0]

        print(animal.produce_sound())

    command = input()

dogs = list(filter(lambda a: isinstance(a, Dog), animals))
cats = list(filter(lambda a: isinstance(a, Cat), animals))
snakes = list(filter(lambda a: isinstance(a, Snake), animals))

sorted_animals = dogs + cats + snakes

[print(animal) for animal in sorted_animals]
