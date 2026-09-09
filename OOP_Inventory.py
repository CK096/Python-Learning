class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"   Price : RM{self.__price:.2f}\n"
                f"   Stock: {self.__stock}")

    def change_price(self,price):
        if price <= 0:
            print("Price Must Greater Than 0")
            return False
        else:
            self.__price = price
            print(f"Price {self.name} Amend to RM{self.__price:.2f} Success!")
            return True

    def add_stock(self,qty):
        if qty < 1:
            print("Prompt Error")
            return False
        else:
            self.__stock += qty
            print(f"Stock {self.name} add in stock quantity {qty} success")
            return True

    def remove_stock(self,stock):
        if stock > self.__stock:
            return False
        else:
            self.__stock -= stock
            return True

    def sell(self,sell):
        if self.remove_stock(sell):
            print(f"{self.name} sell {sell} Success")
        else:
            print("Stock Not Enough")

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

class Inventory:
    def __init__(self):
        self.products = []

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
            if item.title().strip() == product.name:
                self.products.pop(index)
                print(f"{item} Delete Success")
                return True

        print("Product Not Found")
        return False

    def edit_product_price(self,name,price):
        name = name.title().strip()
        for product in self.products:
            if name == product.name:
                if product.change_price(price):
                    return True
                else:
                    return False

        print("Product Not Found")
        return False

    def add_stock2 (self,name,stock):
        name = name.title().strip()
        for product in self.products:
            if name == product.name:
                return product.add_stock(stock)

        print("Product Not Found")
        return False

    def remove_stock(self,name,stock):
        name = name.title().strip()
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

def error_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error")




inventory = Inventory()

while True:
    choice = error_int("===== Inventory Management System =====\n"
                        "1. Add Product\n"
                        "2. View Product\n"
                        "3. Search Product\n"
                        "4. Delete Product\n"
                        "5. Edit Price\n"
                        "6. Add Stock\n"
                        "7. Remove Stock\n"
                        "8. Exit\n"
                        "Enter Your Choice: ")
    if choice == 1:
        name = input("Product Name: ").title().strip()
        price = error_float("Product price: RM")
        stock = error_int("Stock Quantity: ")
        product = Product(name,price,stock)
        inventory.add_product(product)

    elif choice == 2:
        inventory.view_products()

    elif choice == 3:
        search = input("Key In Product You Search: ")
        inventory.search_product(search)

    elif choice == 4:
        inventory.view_products()
        delete = input("Key In Product You Want Remove: ")
        inventory.delete_product(delete)

    elif choice == 5:
        name = input("Product Name: ")
        price = error_float("Product Price: RM")
        inventory.edit_product_price(name,price)

    elif choice == 6:
        name = input("Product Name: ")
        stock = error_int("Stock Qty Add: ")
        inventory.add_stock2(name,stock)

    elif choice == 7:
        name = input("Product Name: ")
        stock = error_int("Stock Qty Remove: ")
        inventory.remove_stock(name, stock)

    elif choice == 8:
        print("Goodbye")
        break
