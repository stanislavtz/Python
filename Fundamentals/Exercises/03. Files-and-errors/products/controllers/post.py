import json


def post_products(path, active_products):
    with open(path, 'w') as file:
        [file.write(json.dumps(product) + '\n') for product in active_products]
