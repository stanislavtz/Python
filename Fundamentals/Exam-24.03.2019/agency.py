from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, id, rooms, baths, square_meters, price):
        self.id = id
        self.rooms = int(rooms)
        self.baths = int(baths)
        self.square_meters = float(square_meters)
        self.price = float(price)
        self.status = 'free'

    @abstractmethod
    def __str__(self):
        return


class LivingApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        super().__init__(id, rooms, baths, square_meters, price)

    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv."


class OfficeApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        super().__init__(id, rooms, baths, square_meters, price)

    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv."


apartments = []
data = input()
while data != 'start_selling':
    try:
        apartment = eval(data)
        apartments.append(apartment)
    except TypeError as err:
        print(err)

    data = input()

exit_points = ['free', 'taken']
data = input()
while not data in exit_points:
    command, id = data.split()

    if not id in list(map(lambda a: a.id, apartments)):
        print(f"Apartment with id - {id} does not exist!")
        data = input()
        continue

    apartment = list(filter(lambda a: a.id == id, apartments))[0]

    if apartment.status == 'taken':
        print(f"Apartment with id - {id} is already taken!")
        data = input()
        continue

    if command == 'rent' and isinstance(apartment, LivingApartment):
        print(f"Apartment with id - {id} is only for selling!")
        data = input()
        continue

    if (command == 'buy' or command == 'hire') and isinstance(apartment, OfficeApartment):
        print(f"Apartment with id - {id} is only for renting!")
        data = input()
        continue

    apartment.status = 'taken'

    data = input()

sorted_apartments = None
if data == 'taken':
    taken_apartments = list(filter(lambda a: a.status == 'taken', apartments))
    sorted_apartments = sorted(taken_apartments, key=lambda a: (a.price, -a.square_meters))
else:
    free_apartments = list(filter(lambda a: a.status == 'free', apartments))
    sorted_apartments = sorted(free_apartments, key=lambda a: (-a.price, a.square_meters))

if len(sorted_apartments) == 0:
    print('No information for this query')
else:
    for ap in sorted_apartments:
        print(ap)
