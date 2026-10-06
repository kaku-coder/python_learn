class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance
        print(f"Your balance is {self.__balance}")

    def deposite(self, amout: float):
        self.__balance += amout
        print(f"Your deposite amout is {amout} and Your balance is {self.__balance}")
    
    def withdorw(self, withrow_balance: float):
        if self.__balance >= withrow_balance:
            self.__balance -= withrow_balance
            print(f"you withdow {withrow_balance} and rest amout is {self.__balance}")
        else:
            print("you dont have sufficint balance ")

    def get_balance(self):
        return self.__balance


person = BankAccount(20000)  # Pass initial balance
person.deposite(5000)        # Deposit money
person.withdorw(3000)        # Withdraw money
print(f"Final Balance: ₹{person.get_balance()}")