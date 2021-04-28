from Costumer import Costumer
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount



def Employee_login():
    #extra anti brute force measure (made for fun)
    n=0
    print("Please enter the login password:")
    choice=input("")
    if choice=="A1234":
        print("nothing for now")
        Employee_menu()
    else:
        while(choice !="A1234"):
            n+=1
            if(n==4):
                print("Too many wrong entries. Access locked.")  
                return;
            else:
                print("Incorrect password. "+str(4-n)+" attempt(s) remaining.")
                choice=input("")
        if choice=="A1234":
            print("nothing for now")
            Employee_menu()

def Employee_menu():
    choice=input("What action do you wish to do:"
               +"\n 1:Create a new costumer account"
               +"\n 2:Delete a costumer account"
               +"\n 3:Get a costumer's details"
               +"\n 4:Change a costumer's bank account balance"
               +"\n 5:Log out\n")
    if choice=="1":
        print("nothing for now")
        #CreateCostumerAccount(firstname,lastname,email)
    elif choice=="2":
        print("nothing for now")
        #DeleteCostumerAccount(accountnumber)
    elif(choice=="3"):
        print("nothing for now")
        #GetCostumerDetails(accountnumber)
    elif(choice=="4"):
        print("nothing for now")
        #ChangeAccountBalance(BankAccount)
    elif(choice=="5"):
        print("Going back to the main menu\n")
        main_menu()
    else:
         print("You must enter a digit between 1 and 5 \nPlease try again")
         Employee_menu()


def main_menu():
    print("********************Welcome To Dorset-Bank********************\n"
    +     "**Please Specify whether you are a costumer or bank employee**")
    choice=input("*          1: Costumer                                       *\n"
                +"*          2: Employee                                       *\n"
                +"**************************************************************\n")
    if choice=="1":
        print("nothing for now")
    elif choice=="2":
        Employee_login()
    else:
        print("You must enter either 1 or 2. \nPlease try again")
        main_menu()

def testcostumer():
    c1=Costumer("Hervé-Henri","Houzard","23857@student.dorset-college.ie")
    print(c1.toString())
#testcostumer()

main_menu()

