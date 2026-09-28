product_id = 1001
product_name = 'Laptop'
category = 'Electronics'
quantity = 15
price = 799.99

print(f"Product ID: {product_id}")
print("Product name: " + product_name)
print("Category: " + category)
print(f"Quantity: {quantity}")
print(f"Price: {price}")

stock_value = quantity * price

print(f"Stock value: {stock_value}")

assortment = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']

for product in assortment:
    print(product)

quantities = [15, 8, 23, 5, 12]

prices = [100, 50, 25, 200, 80]

for qty in quantities:
    print(f"Quantity: {qty + 5}")
    print("Stock checked.")