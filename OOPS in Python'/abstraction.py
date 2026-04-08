class Payment:
    def pay(self):
        print("Processing payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("Processing credit card payment with interest")

class EsewaPayment(Payment):
    def pay(self):
        print("Processing Esewa payment")   

p1 = CreditCardPayment()
p1.pay()
p2 = EsewaPayment()
p2.pay()