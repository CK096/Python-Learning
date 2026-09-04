class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Price : RM{self.__price:.2f}\n"
                f"Stock: {self.__stock}")

    def change_price(self,price):
        if price <= 0:
            print("Price Must Greater Than 0")
        else:
            self.__price = price
            print(f"Price {self.name} Amend to RM{self.__price:.2f} Success!")

    def add_stock(self,qty):
        if qty < 1:
            print("Prompt Error")
        else:
            self.__stock += qty
            print(f"Stock {self.name} add in stock quantity {qty} success")

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
        for product in self.products:
            print(product)

    def search_product(self,item):
        for product in self.products:
            if item.title() == product.name:
                print(product)
                return True

        print("Product Not Found")
        return False

    def delete_product(self,item):
        for index,product in enumerate(self.products):
            if item.title() == product.name:
                self.products.pop(index)
                print(f"{item} Delete Success")
                return True

        print("Product Not Found")
        return False

    def edit_product_price(self,name,price):
        name = name.title()
        for product in self.products:
            if name == product.name:
                product.change_price(price)
                return True

        print("Product Not Found")
        return False

    def add_stock2 (self,name,stock):
        name = name.title()
        for product in self.products:
            if name == product.name:
                product.add_stock(stock)
                return True

        print("Product Not Found")
        return False




product1 = Product("Laptop",3500,10)
product2 = Product("Mouse", 80, 20)
inventory = Inventory()

inventory.add_product(product1)
inventory.add_product(product2)
inventory.search_product("Mouse")
inventory.delete_product("Mouse")
inventory.edit_product_price("Laptop",4000)
inventory.add_stock2("Laptop",5)
inventory.view_products()
