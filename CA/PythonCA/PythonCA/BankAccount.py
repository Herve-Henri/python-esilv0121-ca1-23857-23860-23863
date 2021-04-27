class BankAccount(object):
    #Constructors
    def __init__(self):
        self.name="Unnamed"
        self.balance=0.00

    def __init__(self,name):
        self.name=name
        self.balance=0.00

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    #Properties
    def Name():
        return self.name

    def Balance():
        return self.balance

    #Methods
    def Add(self, n):
        self.balance+=n

    def Withdraw(self, n):
        if(self.balance-n<0):
            println("The account balance cannot be negative, please withdraw a lower amount.")
        else:
            self.balance-=n



