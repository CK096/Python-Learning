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
            print(f"Stock {self.name} add in stock quantity {self.__stock} success")

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



product1 = Product("Laptop",3500,10)
product1.add_stock(5)
product1.change_price(4000)
product1.sell(3)
print(product1.get_price())
print(product1.get_stock())
print(product1)
