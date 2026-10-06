class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def withdrow(self,amount):
        if self.balance>=amount:
            self.balance = self.balance-amount
            print(f"withdrowal sucessful {self.balance}")
        else:
            print(f"insufficient balance {amount}")
    

class SavingAccount(BankAccount):
    def withdrow(self,amount):
        if amount<500:
            print("minimum withdrowal is 500")
        else:
            super().withdrow(self.balance)



account = SavingAccount("Prakash", 5000)
account.withdrow(300)
account.withdrow(2000)
account.withdrow(5000)