from abc import ABC, abstractmethod  #to achieve abstraction

#Encapsulation
class Bank:
    def __init__(self,owner, bal):
        self.__owner = owner #private attribute
        self.__bal = bal

    #getter
    def get_bal(self):
        return self.__bal

    #setter
    def deposit(self, bal):
        self.__bal = bal

account = Bank("ABC", 1000)
print(account.get_bal())  #getter

account.deposit(10000) #setter
print(account.get_bal())

#Abstraction
class Bank:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    # Getter to access balance
    def get_balance(self):
        return self.__balance

    # Abstraction: Setter (Deposit method with hidden logic)
    def deposit(self, amount):
        if amount > 0:
            fee = self.calculate_fee(amount)
            self.__balance += amount - fee
            print(f"Deposited {amount}. Fee of {fee} applied. New balance is {self.__balance}.")
        else:
            print("Invalid deposit amount. Must be greater than 0.")

    def calculate_fee(self, amount):
        return amount * 0.02

    # Abstraction: Allows access to owner's name
    def get_owner(self):
        return self.__owner

account = Bank("ABC", 1000)

#Getter
print(f"Current balance: {account.get_balance()}")

# Deposit with abstraction
account.deposit(500)  # Deposit with 500 amount

#Getter
print(f"Updated balance: {account.get_balance()}")