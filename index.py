class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance=0.0

    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
hesap=BankAccount("Umut")

print(hesap.getBalance())
hesap.deposit(1000)
print(hesap.getBalance())
hesap.withdraw(500)
print(hesap.getBalance())
    


    
