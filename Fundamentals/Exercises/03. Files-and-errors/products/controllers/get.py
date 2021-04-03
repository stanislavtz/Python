import json


def get_products(path):
    with open(path, 'r') as file:
        products = [json.loads(product) for product in file.readlines()]
    return products
