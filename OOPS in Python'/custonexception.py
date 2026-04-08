class InsufficientbalanceError(Exception):
    pass
class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientbalanceError("Insufficient balance for withdrawal")
        self.balance-=amount
        print("withdraw Sucessful. Current balance:", self.balance)

try:
    acc1=BankAccount(1000)
    acc1.withdraw(1500)

except InsufficientbalanceError as e:
    print("Error:", e)