def add_product(product, searched, active_products):
    if(searched):
        product['quantity'] += searched[1]['quantity']
        active_products[searched[0]] = dict(product)
    else:
        active_products.append(product)
