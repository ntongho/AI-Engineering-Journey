# Parent:
# Payment

# Method:
# pay()

# Children:
# CardPayment
# CashPayment
# CryptoPayment

# Each prints a different payment message.

# Loop through them.
# Call:
# payment.pay()



class Payment:
    def pay(self):
        pass

class CardPayment(Payment):

    def pay(self):
        print("Card payment Successful")

class  CashPayment(Payment):

    def pay(self):
        print("Cash payment Successful")

class CryptoPayment(Payment):

     def pay(self):
          print("Crypto payment Successful")


payments = [CardPayment(),CashPayment(),CryptoPayment()]

for payment in payments:
    payment.pay()
         