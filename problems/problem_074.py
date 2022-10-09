# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# There is pseudocode for you to guide you.

# class BankAccount
    # method initializer(self, balance)
        # self.balance = balance

    # method get_balance(self)
        # returns the balance

    # method withdraw(self, amount)
        # reduces the balance by the amount

    # method deposit(self, amount)
        # increases the balance by the amount

class BankAccount:
    # You always start with the innit function. Determine the parameters for each function
    #The function below only onyl estalbishes self.balance. It doesn't do anything else
    def __init__(self, balance):
        self.balance = balance

#in order to get the actual return you have to make another function that returns the balance
    def get_balance(self):
        return self.balance
#For withdrwa balance you have to refer to the first function
#you also establish which paramters need to be added.
#THE AMOUNT IS FOR THE INPUT FROM THE USER FOR DEPOSIT AND WITHDRAWING
    def withdraw_balance(self, amount):
        self.balance = self.balance - amount
#For the deposit you als orefer to the same function
# This time amoumnt will be used to add to the balance
    def deposit_balance(self, amount):
        self.balance = self.balance + amount



account = BankAccount(100)

print(account.get_balance())  # prints 100

account.withdraw_balance(50)
print(account.get_balance())  # prints 50

account.deposit_balance(120)
print(account.get_balance())  # prints 170