from logging import setLogRecordFactory
from os import supports_effective_ids
class Payment:
    def __init__(self,amount:int)->None: 
        self.amount = amount

    def pay(self,discount=0):
        self.amount=self.amount-discount
        print(f"final amount is {self.amount}")
        print(f"discount amount is {discount}")

# CreditCardPayment
class CreditCardPayment(Payment):
    def pay(self,discoiunt=0,processcingFees = 20):
        super().pay(discoiunt)
        self.amount=self.amount+processcingFees
        print(f"processing fee added is {processcingFees}")
        print(f"total final amount is {self.amount}")


# UPIPayment
class UpiPayment(Payment):
    def pay(self,discount=0):
        processingfees = 0
        super().pay(discount)
        print(self.amount)





paymentMethod = Payment(1000)
paymentMethod.pay(100)
card = CreditCardPayment(1000)
card.pay(100)
upi = UpiPayment(1000)
upi.pay(100)