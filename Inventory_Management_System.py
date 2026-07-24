products = []

def product_empty(name):
    if not name:
        print("Name Cannot Be Empty!")
        return True
    return False

def error_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Stock Quantity!")

def error_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Price!")




while True:
    name = input("Product Name: ").strip().title()
    if product_empty(name):
        continue
    price = error_float("Price: RM")
    if price <= 0:
        print("Price Cannot Below Than RM 0.01")
        continue
    stock = error_int("Stock Quantity: ")
    if stock < 0:
        print("Stock Cannot Be Negative")
        continue
    products.append({"name": name,"price": price,"stock": stock})

    
    print("===== Product List =====")
    for index, product in enumerate(products):
        print(f"{index+1}.{product["name"]} \n"
              f"Price : RM{product["price"]:.2f}\n"
              f"Stock : {product["stock"]}")
