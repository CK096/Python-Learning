import json

class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"   Price : RM{self.__price:.2f}\n"
                f"   Stock: {self.__stock}")

    def to_dict(self):
        return {"name": self.name,
                "price": self.get_price(),
                "stock": self.get_stock()}

    def change_price(self,price):
        if price <= 0:
            print("Price Must Greater Than 0")
            return False

        self.__price = price
        print(f"Price {self.name} Amend to RM{self.__price:.2f} Success!")
        return True

    def add_stock(self,qty):
        if qty < 1:
            print("Prompt Error")
            return False

        self.__stock += qty
        print(f"Stock {self.name} add in stock quantity {qty} success")
        return True

    def remove_stock(self,stock):
        if stock > self.__stock or stock < 1:
            return False

        self.__stock -= stock
        return True

    def sell(self,sell):
        if self.remove_stock(sell):
            print(f"{self.name} sell {sell} Success")
            return True

        print("Stock Not Enough")
        return False

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

class FoodProduct(Product):
    def __init__(self,name,price,stock,expired):
        super().__init__(name,price,stock)
        self.expired = expired

    def __str__(self):
        return super().__str__() + f"\n   Expired Date: {self.expired}"

    def to_dict(self):
        data = super().to_dict()
        data["expired_date"] = self.expired
        return data

class ElectronicProduct(Product):
    def __init__(self,name,price,stock,warranty):
        super().__init__(name,price,stock)
        self.warranty = warranty

    def __str__(self):
        return super().__str__ () + f"\nWarranty : {self.warranty}"

    def to_dict(self):
        data = super().to_dict()
        data["warranty"] = self.warranty
        return data

class Inventory:
    def __init__(self):
        self.products = []

    def to_list(self):
        products_list = []
        for product in self.products:
            item = product.to_dict()
            products_list.append(item)

        return products_list

    def save_json(self):
        path_file = r"C:\Users\user\Desktop\workshop\oop.inventory.json"
        product_list = self.to_list()

        with open(path_file, "w", encoding="utf8") as file:
            json.dump(product_list,file,indent=4,ensure_ascii=False)

    def load_json(self):
        path_file = r"C:\Users\user\Desktop\workshop\oop.inventory.json"
        with open(path_file, "r", encoding="utf8") as file:
            products = json.load(file)

        for data in products:
            name = data["name"]
            price = data["price"]
            stock = data["stock"]
            if "expired_date" in data:
                expired_stock = data["expired_date"]
                product = FoodProduct(name, price, stock,expired_stock)
            else:
                product = Product(name, price, stock)
            self.add_product(product)

    def add_product(self,product):
        self.products.append(product)

    def view_products(self):
        for index, product in enumerate(self.products):
            print(f"{index+1}. {product}\n\n")

    def search_product(self,item):
        for product in self.products:
            if item.title().strip() == product.name:
                print(product)
                return True

        print("Product Not Found")
        return False

    def delete_product(self,item):
        for index,product in enumerate(self.products):
            if item == product.name:
                self.products.pop(index)
                print(f"{item} Delete Success")
                return True

        print("Product Not Found")
        return False

    def edit_product_price(self,name,price):
        for product in self.products:
            if name == product.name:
                return product.change_price(price)

        print("Product Not Found")
        return False

    def add_stock(self,name,stock):
        for product in self.products:
            if name == product.name:
                return product.add_stock(stock)

        print("Product Not Found")
        return False

    def remove_stock(self,name,stock):
        for product in self.products:
            if name == product.name:
                if product.remove_stock(stock):
                    print("Remove Success")
                    return True
                else:
                    print("Not Enough Stock")
                    return False
        print("Product Not Found")
        return False

def error_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Quantity Cant Be Negative")
            else:
                return value

        except ValueError:
            print("Error")

def valid_int(prompt,min_value,max_value):
    while True:
        try:
            value = int(input(prompt))

            if min_value <= value <= max_value:
                return value
            else:
                print(f"Prompt can use on {min_value} to {max_value} only")

        except ValueError:
            print("Error")

def error_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error")

def input_name(prompt):
    name = input(prompt).title().strip()
    return name




inventory = Inventory()
inventory.load_json()

food1 = FoodProduct("Milk", 3.2,50,"11/11/2026")


while True:
    save = False

    choice = valid_int("===== Inventory Management System =====\n"
                        "1. Add Product\n"
                        "2. View Product\n"
                        "3. Search Product\n"
                        "4. Delete Product\n"
                        "5. Edit Price\n"
                        "6. Add Stock\n"
                        "7. Remove Stock\n"
                        "8. Exit\n"
                        "Enter Your Choice: ",1,8)
    if choice == 1:
        product_type = valid_int("===== Product Type =====\n"
                                 "1.Normal Product\n"
                                 "2.Food Product\n"
                                 "Enter Type: ",1,2)
        name = input_name("Product Name: ")
        price = error_float("Product price: RM")
        stock = error_int("Stock Quantity: ")
        if product_type == 1:
            product = Product(name,price,stock)
        elif product_type == 2:
            expired_date = input_name("Expired Date: ")
            product = FoodProduct(name,price,stock,expired_date)
        inventory.add_product(product)
        save = True

    elif choice == 2:
        inventory.view_products()

    elif choice == 3:
        search = input_name("Key In Product You Search: ")
        inventory.search_product(search)

    elif choice == 4:
        inventory.view_products()
        delete = input_name("Key In Product You Want Remove: ")
        inventory.delete_product(delete)
        save = True

    elif choice == 5:
        inventory.view_products()
        name = input_name("Product Name: ")
        price = error_float("Product Price: RM")
        inventory.edit_product_price(name,price)
        save = True

    elif choice == 6:
        inventory.view_products()
        name = input_name("Product Name: ")
        stock = error_int("Stock Qty Add: ")
        inventory.add_stock(name,stock)
        save = True

    elif choice == 7:
        inventory.view_products()
        name = input_name("Product Name: ")
        stock = error_int("Stock Qty Remove: ")
        inventory.remove_stock(name, stock)
        save = True

    elif choice == 8:
        print("Goodbye")
        break

    if save:
        inventory.save_json()
