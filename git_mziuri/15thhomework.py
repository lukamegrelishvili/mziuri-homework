class Bank_Account:
    def __init__(self, account_name):
        self.__account_name = account_name
        self.__balance = 0

    def get_account_name(self):
        return self.__account_name

    def set_account_name(self, new_name):
        self.__account_name = new_name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Current balance after replenishment: {self.__balance} GEL")
        else:
            print("The replenishment amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Current balance after withdraw: {self.__balance} GEL")
            else:
                print(f"Insufficient funds. Available balance: {self.__balance} GEL")
        else:
            print("The replenishment amount must be positive number.")


    def get_balance(self):
        return self.__balance


account = Bank_Account("Giorgi Abashidze")
print(f"name of bank account: {account.get_account_name()}")
account.deposit(100)
print(f"current balance: {account.get_balance()} GEL")
account.withdraw(30)
print(f"current balance: {account.get_balance()} GEL")
