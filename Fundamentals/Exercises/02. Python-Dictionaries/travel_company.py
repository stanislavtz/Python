def calculate_city_seats(obj):
    return sum(obj.values())


cities = {}
data = input()
while data != 'ready':
    city = data.split(':')[0]
    v_data = data.split(':')[1].split(',')

    if not city in cities:
        cities[city] = {}

    for v in v_data:
        v_type = v.split('-')[0]
        v_capacity = int(v.split('-')[1])
        cities[city][v_type] = v_capacity

    data = input()

result = []
data = input()
while data != 'travel time!':
    city = data.split()[0]
    people = int(data.split()[1])
    seats = calculate_city_seats(cities[city])

    if people < seats:
        result.append(f"{city} -> all {people} accommodated")
    else:
        result.append(f"{city} -> all except {people - seats} accommodated")

    data = input()

print("\n".join(result))