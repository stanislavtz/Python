def find_product(product, active_products):
    return next(((i, p) for i, p in enumerate(active_products)
                 if p['name'] == product['name'] and p['type'] == product['type']), None)
