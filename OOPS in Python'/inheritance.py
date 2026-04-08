class payment:
    def __init__(self,amount):
        self.amount=amount
    
    def pay(self):
        print("processing payment of :", self.amount)

class creditcardpayment(payment):
    def pay(self):
        print("Processing credit card payment of:", self.amount, "with interest")

class EsewaPayment(payment):
    def pay(self):
        print("Processing Esewa payment of:", self.amount)

p1=creditcardpayment(500)
p1.pay()

p2=EsewaPayment(1000)
p2.pay()