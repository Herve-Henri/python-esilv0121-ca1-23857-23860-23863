class BankAccount(object):
    #Constructors
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance

    #Properties
    def Name(self):
        return self._name

    def Balance(self):
        return self._balance

    #Methods
    def toString(self):
        return "Account name: "+self._name+"   Account balance:"+str(self._balance)+" €"

    def Add(self, n):
        self._balance+=n

    def Withdraw(self, n):
        if(self._balance-n<0):
            println("The account balance cannot be negative, please withdraw a lower amount.")
        else:
            self._balance-=n



