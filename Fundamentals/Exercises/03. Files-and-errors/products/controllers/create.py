def create_product(data):
    pr_type = data.split()[1]

    if len(data.split()) > 4:
        new_data = input()
        create_product(new_data)
    name = data.split()[0]

    pr_price = data.split()[2]
    if pr_price.replace('.', '').isdigit() == False:
        new_data = input()
        create_product(new_data)
    price = float(pr_price)

    pr_qtty = data.split()[3]

    if pr_qtty.isdigit() == False:
        new_data = input()
        create_product(new_data)
    qtty = int(pr_qtty)

    return {'type': pr_type, 'name': name, 'price': price, 'quantity': qtty}
