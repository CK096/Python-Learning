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
    user_input = input(prompt).strip().title()
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

def price_less_than_0(price):
    if price <= 0:
        print("Price Cannot Below Than RM 0.01")
        return True
    return False

def stock_less_than_0(stock):
    if stock < 0:
        print("Stock Cannot Be Negative")
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
        if price_less_than_0(price):
            continue
        stock = error_int("Stock Quantity: ")
        if stock_less_than_0(stock):
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
        print("===== Edit Products =====")
        view_products_list()
        edit = error_int("Select Number Item Edit: ")
        if len_products(edit):
            continue
        print(f"Current Name : {products[edit-1]["name"]}")
        new_name = edit_name("New Name (Enter 保持原本): ")
        if new_name is not None:
            products[edit - 1]["name"] = new_name
        print(f"Current Price : {products[edit - 1]["price"]:.2f}")
        new_price = edit_price("New Price (Enter 保持原本): ")
        if new_price is not None:
            if price_less_than_0(new_price):
                continue
            products[edit - 1]["price"] = new_price
        print(f"Current Stock : {products[edit - 1]["stock"]}")
        new_stock = edit_stock("New stock (Enter 保持原本): ")
        if new_stock is not None:
            if stock_less_than_0(new_stock):
                continue
            products[edit - 1]["stock"] = new_stock
        save_products()

    elif choice == 6:
        print("Thanks for using Inventory Management System")
        save_products()
        break
