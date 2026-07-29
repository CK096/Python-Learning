def save_products():
    with open(path_file,"w") as file:
        for product in products:
            file.write(f"{product['name']},{product['price']},{product['stock']}\n")

def load_products():
    try:
        with open(path_file,"r") as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                price = float(data[1])
                stock = int(data[2])
                products.append({"name": name, "price": price, "stock": stock})
    except FileNotFoundError:
        pass

def product_empty(name):
    if not name:
        print("Name Cannot Be Empty!")
        return True
    return False

def products_empty():
    if not products:
        print("List is empty!")
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

def edit_price(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "":
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid Price!")

def edit_name(prompt):
    user_input = input(prompt)
    if user_input == "":
        return None
    return user_input

def edit_stock(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "":
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid Stock")

def len_products(number):
    if number < 1 or number > len(products):
        print("Invalid Product Number")
        return True
    return False

def view_products_list():
    for index, product in enumerate(products):
        print(f"{index + 1}. {product["name"]} \n"
              f"   Price : RM{product["price"]:.2f}\n"
              f"   Stock : {product["stock"]}\n"
              f" ")


products = []
path_file = r'C:\Users\user\Desktop\workshop\Inventory_Management_System.txt'
load_products()

while True:
    choice = error_int(f"===== Inventory Management System =====\n"
                       f"1. Add Product\n"
                       f"2. View Product\n"
                       f"3. Search Product\n"
                       f"4. Delete Products\n"
                       f"5. Edit Products\n"
                       f"6. Exit\n"
                       f"====================\n"
                       f"Choice : ")
    if choice == 1:
        name = input("Product Name: ").strip().title()
        if product_empty(name):
            continue
        price = error_float("Price: RM ")
        if price <= 0:
            print("Price Cannot Below Than RM 0.01")
            continue
        stock = error_int("Stock Quantity: ")
        if stock < 0:
            print("Stock Cannot Be Negative")
            continue
        products.append({"name": name,"price": price,"stock": stock})
        save_products()

    elif choice == 2:
        if products_empty():
            continue
        print("===== Product List =====")
        view_products_list()

    elif choice == 3:
        if products_empty():
            continue
        found = False
        print("===== Search Product =====")
        search = input("Search: ").strip().title()
        if product_empty(search):
            continue
        for product in products:
            if search == product["name"]:
                print(f"Product Found\n"
                      f"{product['name']}\n"
                      f"Price : RM {product['price']:.2f}\n"
                      f"Stock : {product['stock']}")
                found = True
        if not found :
            print("Product Not Found")

    elif choice == 4:
        if products_empty():
            continue
        print("===== Delete Products =====")
        view_products_list()
        delete = error_int("Select Product Number: ")
        if len_products(delete):
            continue
        delete_name = products[delete-1]["name"]
        del products[delete-1]
        print(f"Delete Success!\n"
              f"{delete_name} has been removed")
        save_products()

    elif choice == 5:
        if products_empty():
            continue
        print("===== Delete Products =====")
        view_products_list()
        edit = error_int("Select Number Item Edit: ")
        if len_products(edit):
            continue
        # 到这里写了一半

    elif choice == 6:
        print("Thanks for using Inventory Management System")
        save_products()
        break
