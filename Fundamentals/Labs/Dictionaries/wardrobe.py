wardrobe = {}
n = int(input())

for i in range(n):
    data = input()
    color = data.split(' -> ')[0]
    items = data.split(' -> ')[1].split(',')

    if not color in wardrobe:
        wardrobe[color] = []

    wardrobe[color] += items

searched = input()
s_color = searched.split()[0]
s_item = searched.split()[1]

for color, items in wardrobe.items():
    print(f"{color} clothes:")
    for item in sorted(set(items), key=items.index):
        if color == s_color and item == s_item:
            print(f"* {item} - {items.count(item)} (found!)")
        else:
            print(f"* {item} - {items.count(item)}")
