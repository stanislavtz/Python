class Card:
    def __init__(self, owner, number):
        self.owner = owner
        self.number = number


class Ticket:
    def __init__(self, destination, price, card=None):
        self.destination = destination
        self.price = self.set_price(price, card)
        self.card = card

    def set_price(self, price, card):
        if card == None:
            return price
        return price / 2


class Person:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.tickets = []

    def get_total_sum(self):
        return sum(list(map(lambda t: t.price, self.tickets)))

    def __str__(self):
        result = [f"{self.name}:"]

        sorted_tickets = sorted(self.tickets, key=lambda t: t.price, reverse=True)
        for ticket in sorted_tickets:
            ticket_line = (f"--{ticket.destination}: {ticket.price:.2f}lv")
            if ticket.card:
                ticket_line += f" (using card {ticket.card})"

            result.append(ticket_line)   
        result.append(f"total: {sum(list(map(lambda t: t.price, self.tickets))):.2f}lv")

        return '\n'.join(result)
    

people = []
existing_cards = []

n = int(input())
for _ in range(n):
    data = input().split()
    first_name, last_name, card_number = data
    full_name = first_name + ' ' + last_name
    card = Card(full_name, card_number)
    existing_cards.append(card)

data = input()
while data != 'time to leave!':
    _, first_name, last_name, destination, card_number = data.split()
    full_name = first_name + ' ' + last_name
    price = sum(list(map(ord, destination))) / 100
    
    person = None
    filtered_people = list(filter(lambda p: p.name == full_name, people))
    if len(filtered_people) > 0:
        person = filtered_people[0]
    else:
        person = Person(full_name)
        people.append(person)

    filtered_cards = list(filter(lambda c: c.number == card_number, existing_cards))
    if len(filtered_cards) > 0:
        card = filtered_cards[0]
        if card.owner != full_name:
            print(f"card {card_number} already exists for another passenger!")
            ticket = Ticket(destination, price)
            person.tickets.append(ticket)
        else:
            ticket = Ticket(destination, price, card_number)
            person.cards.append(card)
            person.tickets.append(ticket)
    else:
        is_valid = sum(list(map(int, card_number))) % 7 == 0
        if is_valid == False:
            print(f"card {card_number} is not valid!")
            ticket = Ticket(destination, price)
            person.tickets.append(ticket)
        else:
            print(f"issuing card {card_number}")
            card = Card(full_name, card_number)
            existing_cards.append((card))
            ticket = Ticket(destination, price, card_number)
            person.cards.append(card)
            person.tickets.append(ticket)

    data = input()

sorted_people = sorted(people, key=lambda p: p.get_total_sum(), reverse=True)
for person in sorted_people:    
    if len(person.tickets) > 0:
        print(person)