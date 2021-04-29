class BankAccount(object):
    #Constructors
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance

    #Properties
    def Name():
        return self._name

    def Balance():
        return self._balance

    #Methods
    def toString(self):
        return "Account name: "+self.name+"   Account balance:"+str(self.balance)+" €"

    def Add(self, n):
        self.balance+=n

    def Withdraw(self, n):
        if(self.balance-n<0):
            println("The account balance cannot be negative, please withdraw a lower amount.")
        else:
            self.balance-=n



