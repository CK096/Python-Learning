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
            print("Error")

def error_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Price!")

def view_products_list():
    for index, product in enumerate(products):
        print(f"{index + 1}.{product["name"]} \n"
              f"  Price : RM{product["price"]:.2f}\n"
              f"  Stock : {product["stock"]}\n"
              f" ")




while True:
    choice = error_int(f"===== Inventory Management System =====\n"
                       f"1. Add Product\n"
                       f"2. View Product\n"
                       f"3. Exit\n"
                       f"====================\n"
                       f"Choice : ")
    if choice == 1:
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

    if choice == 2:
        print("===== Product List =====")
        view_products_list()

    if choice == 3:
        exit()
