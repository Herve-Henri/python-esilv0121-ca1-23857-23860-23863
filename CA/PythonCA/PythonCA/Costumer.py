class Costumer(object):
    #Constructor
    def __init__(self,firstname,lastname,email):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        #self.accountnumber=GenerateAccountNumber()
        #self.pincode=GeneratePincode()
        self.bankaccount=BankAccount()



