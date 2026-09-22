class BankAccount:
    def __init__(self,balance,accountNo):
        self.balance = balance
        self.accountNo=accountNo
    
    # debit method
    
    def DbitMethod(self,amout):
        self.balance-=amout
        print("Rs.",amout,"was debited")
        print("Rs.",self.balance,"rest balance")
    
    def CreditMethod(self,amout):
        self.balance+=amout
        print("Rs.",amout,"was credited")
        print("Rs.",self.balance,"rest balance")
    
    def CheckBalance(self):
        return self.balance
        # print("Rs.",amout,"was debited")
        return print("Rs.",self.balance,"rest balance")


acc1 = BankAccount(5000,1231231)
acc1.DbitMethod(2000)
acc1.CreditMethod(7000)
print(acc1.CheckBalance())
