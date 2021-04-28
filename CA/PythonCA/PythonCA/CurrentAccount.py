from BankAccount import BankAccount

class CurrentAccount(BankAccount):
   #Constructor
    def __init__(self,name,balance):
        super().__init__(name,balance)

    #Methods