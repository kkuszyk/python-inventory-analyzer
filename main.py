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

def calculate_stock_value(quantity, price):

    output = quantity * price

    print(output)

calculate_stock_value(20, 100)


