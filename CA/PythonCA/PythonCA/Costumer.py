from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

class Costumer(object):
    #Constructor
    def __init__(self,firstname,lastname,email):
        self.__firstname=firstname
        self.__lastname=lastname
        self.__email=email
        self.__accountnumber=self.GenerateAccountNumber(firstname,lastname)
        self.__pincode=self.GeneratePinCode(firstname,lastname)
        self.__savings=SavingsAccount(self.__accountnumber+"-savings",0.00)
        self.__current=CurrentAccount(self.__accountnumber+"-current",0.00)

    #Basic Properties
    def Fullname(self):
        return self.__firstname+" "+self.__lastname

    def Email(self):
        return self.__email

    def Accountnumber(self):
        return self.__accountnumber

    def Pincode(self):
        return self.__pincode

    def Savings(self):
        return self.__savings

    def Current(self):
        return self.__current

    #Methods
    def GetAlphabPosition(self,letter):
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
            position=("12")
        elif(letter=='M' or letter=='m'):
            position=("13")
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

    def GenerateAccountNumber(self,firstname,lastname):
        an=(firstname[0].lower()+lastname[0].lower()+"-"+str(len(firstname+lastname))+"-"+self.GetAlphabPosition(firstname[0])+"-"
           + self.GetAlphabPosition(lastname[0]))
        return an

    def GeneratePinCode(self,firstname,lastname):
        pin=self.GetAlphabPosition(firstname[0])+self.GetAlphabPosition(lastname[0])
        return pin

    def toString(self):
        return ("Firstname: "+self.__firstname+"    Lastname: "+self.__lastname+"    Email: "+self.__email
                + "\nAccount number: "+self.__accountnumber+"    Pin code: "+self.__pincode 
                + "\nSavings account: "+self.__savings.toString()
                + "\nCurrent account: "+self.__current.toString())
   

    
    


        

    




         




