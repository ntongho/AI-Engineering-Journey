# Create:
# Payment

# It must:
# inherit from ABC
# contain an abstract method called pay()
# Children

# Create:
# CardPayment
# CashPayment
# CryptoPayment

# Each should inherit from Payment.
# Each must implement:
# pay()
# Give each a different output.

# For example:
# Card payment successful.
# Cash payment successful.
# Crypto payment successful.

# Then:
# payments = [
#     CardPayment(),
#     CashPayment(),
#     CryptoPayment()
# ]

# Loop through them:
# for payment in payments:
#     payment.pay()




from abc import ABC, abstractmethod


class Payment(ABC):



    @abstractmethod
    def pay(self):
        pass

class CardPayment(Payment):

    def pay(self):
        print("card payment successful")



class CashPayment(Payment):

    def pay(self):
        print("cash payment successful")


class CryptoPayment(Payment):

    def pay(self):
        print("crypto payment successful")

payments = [
    CardPayment(), 
    CashPayment(), 
    CryptoPayment()
    ]

for payment in payments:
    payment.pay()


    


