def product_details(name,product_id,price,quantity):
    result=(
        f"Product Name: {name}\n"
        f"Product ID: {product_id}\n"
        f"Price: {price}\n"
        f"Quantity: {quantity}\n"
    )
    return result
if __name__=="__main__":
    name="Laptop"
    product_id="P456"
    price=1200
    quantity=10
    print(product_details(name,product_id,price,quantity))