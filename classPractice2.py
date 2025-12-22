class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
        print("Balance",balance)
        
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs" ,amount, "debited")
        print("total balance",self.total_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs" ,amount, "Credited")
        print("total balance",self.total_balance())

    def total_balance(self):
        return self.balance



a1 = Account(100,123)
a2 = Account(100,124)

a1.debit(200)
print(a1.balance)
