import product_controllers
import calculate_sales
import analyze_db

path = 'products/products_db.txt'
products = product_controllers.get.get_products(path)
active_products = list(products)

outputs = []

products_types = ["Food", "Electronics", "Domestics"]

data = input()
while data != 'exit':
    if len(data.split()) > 1 and data.split()[1] in products_types:
        product = product_controllers.create.create_product(data)
        searched = product_controllers.search.find_product(product, active_products)
        product_controllers.add.add_product(product, searched, active_products)
    elif data == 'stock':
        product_controllers.post.post_products(path, active_products)
    elif data == 'sales':
        sales = {"Food": 0, "Electronics": 0, "Domestics": 0}
        calculate_sales.calculate_sales(sales, products_types, active_products)
        sorted_sales = sorted(sales, key=lambda k: sales[k], reverse=True)
        [outputs.append(f"{k}: ${sales[k]:2g}") for k in sorted_sales if sales[k] != 0]
    elif data == 'analyze':
        products = product_controllers.get.get_products(path)
        [outputs.append(product)
         for product in analyze_db.do_analyze(products)]
    data = input()

print('\n'.join(outputs))
