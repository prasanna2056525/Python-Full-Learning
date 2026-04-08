'''class BankAccount:
        def __init__(self,name,balance):
            self.name=name
            self.balance=balance
        
    acc1 =BankAccount("Ram",1000)
    acc1.balance = 10000
    print(acc1.name, acc1.balance)

    class BankAccount:
        def __init__(self,name,balance):
            self.name=name
            self.__balance=balance
        
        def get_balance(self):
            return self.__balance
        
        def set_balance(self,amount):
            if amount>=0:
                self.__balance=amount
            else:
                print("Invalid balance amount")
    acc1 =BankAccount("Ram",1000)
    acc1.set_balance(10000)
    print(acc1.name, acc1.get_balance())'''


class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

acc1 = Bankaccount("Ram", 1000)
acc1.deposit(500)
acc1.withdraw(200)
print(f"Current balance for {acc1.name}: {acc1.get_balance()}")



