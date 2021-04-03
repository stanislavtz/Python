def calculate_sales(sales, product_type, active_products):
    for t in product_type:
        for p in active_products:
            if t in p.values():
                sales[t] += p['price'] * p['quantity']