# Now let's introduce methods.

# Create a BankAccount class with:

# owner
# balance

# Create one object:

# Owner = "Prakash"
# Balance = 5000

# Then create a method called deposit() that:

# takes an amount
# adds that amount to the balance
# prints the updated balance

# For example:

# Initial balance: 5000
# Deposit: 2000
# Updated balance: 7000

# Try it yourself. Don't worry if you get stuck—send me your code and I'll check it.


from typing import Self
class BankAccount:
    def __init__(self,owner,balance):
        self.ownder=owner
        self.balance = balance
    def deposite(self,amount):
        self.balance+=amount
        print("updated balance", self.balance)


firstObject = BankAccount("prakash",5000)
print(firstObject.balance)
firstObject.deposite(2000)