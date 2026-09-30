class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount <= 0:
            print("Deposit Amount Must Be Greater Than 0")
            return False
        else:
            self.__balance += amount
            return True

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Withdraw Amount Cant More Than Account Balance")
            return False
        if amount <= 0:
            print("Withdraw Amount Cant Be Negative Amount")
            return False
        else:
            self.__balance -= amount
            return True

    def __str__(self):
        return (f"Owner Name: {self.owner}\n"
                f"Account Balance: RM{self.__balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.interest_rate}"

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate

    def add_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)



account = SavingsAccount("Kok", 1000,0.05)

account.add_interest()
print(account.get_balance())
print(account.calculate_interest())
print(account)
