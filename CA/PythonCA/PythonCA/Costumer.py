class Costumer(object):
    #Methods
    def GetAlphabPosition(letter):
        #Note: We aren't using the function string.ascii_lowercase.index because we want a string and not an integer
        position="-1"
        if(letter=='A' or letter=='a'):
            position="01"
        elif(letter=='B' or letter=='b'):
            position="02"
        elif(letter=='C' or letter=='c'):
            position="03"
        elif(letter=='D' or letter=='d'):
            position="04"
        elif(letter=='E' or letter=='e'):
            position="05"
        elif(letter=='F' or letter=='f'):
            position="06"
        elif(letter=='G' or letter=='g'):
            position="07"
        elif(letter=='H' or letter=='h'):
            position="08"
        elif(letter=='I' or letter=='i'):
            position="09"
        elif(letter=='J' or letter=='j'):
            position=("10")
        elif(letter=='K' or letter=='k'):
            position("11")
        elif(letter=='L' or letter=='l'):
            position("12")
        elif(letter=='M' or letter=='m'):
            position("13")
        elif(letter=='N' or letter=='n'):
            position=("14")
        elif(letter=='O' or letter=='o'):
            position=("15")
        elif(letter=='P' or letter=='p'):
            position=("16")
        elif(letter=='Q' or letter=='q'):
            position=("17")
        elif(letter=='R' or letter=='r'):
            position=("18")
        elif(letter=='S' or letter=='s'):
            position=("19")
        elif(letter=='T' or letter=='t'):
            position=("20")
        elif(letter=='U' or letter=='u'):
            position=("21")
        elif(letter=='V' or letter=='v'):
            position=("22")
        elif(letter=='W' or letter=='w'):
            position=("23")
        elif(letter=='X' or letter=='x'):
            position=("24")
        elif(letter=='Y' or letter=='y'):
            position=("25")
        elif(letter=='Z' or letter=='z'):
            position=("26")
        return position

    def GenerateAccountNumber(firstname,lastname):
        an=(firstname[0]+lastname[0]+"-"+str((firstname+lastname).length)+"-"+GetAlphabPosition(firstname[0])+"-"
           + GetAlphabPosition(lastname[0]))
        return an

    def GeneratePinCode(firstname,lastname):
        pin=GetAlphabPosition(firstname[0])+GetAlphabPosition(lastname[0])
        return pin

    def toString():
        return ("Firstname: "+self.firstname+" Lastname: "+self.lastname+" Email: "+self.email
                + "\nAccount number: "+self.accountnumber+" Pin code: "+self.pincode 
                + "\nSavings account: "+self.savings.toString()+" Current account: "+self.current.toString())

    #Constructor
    def __init__(self,firstname,lastname,email):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.accountnumber=GenerateAccountNumber(firstname,lastname)
        self.pincode=GeneratePincode(firstname,lastname)
        self.savings=SavingsAccount(accountnumber+"-savings")
        self.current=CurrentAccount(accountnumber+"-current")

    #Basic Properties
    def Fullname():
        return self.firstname+" "+self.lastname

    def Email():
        return self.email

    def Accountnumber():
        return self.accountnumber

    def Pincode():
        return self.pincode

    def Savings():
        return self.savings

    def Current():
        return self.current
   

    
    


        

    




         




