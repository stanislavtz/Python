from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if int(age) < 0:
            raise Exception('Invalid input!')
        self.__age = age

    @abstractmethod
    def produce_sound(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"{self.name} {self.age} {self.gender}\n{self.produce_sound()}"


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return 'Meow meow'

    def __str__(self):
        return f"Cat\n{super().__str__()}"


class Tomcat(Cat):
    def _init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return 'MEOW'

    def __str__(self):
        return f"Tomcat\n{super().__str__()[4:]}"


class Kitten(Cat):
    def _init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return 'Meow'

    def __str__(self):
        return f"Kitten\n{super().__str__()[4:]}"


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return 'Woof!'

    def __str__(self):
        return f"Dog\n{super().__str__()}"


class Frog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return 'Ribbit'

    def __str__(self):
        return f"Frog\n{super().__str__()}"


def create_animal(string, gender):
    if string in ['Cat', 'Tomcat', 'Kitten']:
        if gender == 'Tomcat' or string == 'Tomcat':
            return Tomcat(name, age, 'Male')

        if gender == 'Kitten' or string == 'Kitten':
            return Kitten(name, age, 'Female')

        return Cat(name, age, gender)

    elif string == 'Dog':
        return Dog(name, age, gender)
    elif string == 'Frog':
        return Frog(name, age, gender)
    else:
        raise Exception('Invalid input!')


animals = []
input_str = input()
while input_str != 'Beast!':
    try:
        name, age, gender = input().split()
        animal = create_animal(input_str, gender)
        animals.append(animal)

        input_str = input()

    except Exception as ex:
        print(ex)
        input_str = input()

[print(animal) for animal in animals]
