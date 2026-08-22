class Product:
    def __init__ (self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Item : {self.name}\n"
              f"Price :RM {self.price:.2f}\n"
              f"Stock : {self.stock}")
    def change_price(self,new_price):
        self.price = new_price
    def add_stock(self,amount):
        self.stock += amount

    def remove_stock(self,amount):
        if amount > self.stock:
            return False
        else:
            self.stock -= amount
            return True

    def sell(self,amount):
       if self.remove_stock(amount):
           print(f"Sold {amount} {self.name} Success")
       else:
           print(f"No Enough Stock")


product1 = Product("Laptop",3500,10)
product1.change_price(4000)
product1.sell(3)
product1.display()
