from Costumer import Costumer
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
import os
from os import path

def CheckValidName(name):
    #A name is valid if it is less than 30 characters in length and doesn't contain any special character apart from '-'
    valid = True
    if(len(name)>30):
        valid=False
    for character in name:
        if(character.isalpha()==False):
            if character!="-":
                valid=False
    return valid

def CheckValidEmail(email):
    #An email is valid if it is less than 50 characters in length and contains the character '@'
    valid = True
    if(len(email)>50):
        valid=False
    if(email.find('@')==-1):
        valid=False
    return valid

def CreateCostumerAccount():
    firstname=input("Please enter the costumer's firstname.\n")
    while(CheckValidName(firstname)==False):
        firstname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        if(firstname=="0"):
            print("")
            Employee_menu()
            return
    lastname=input("Please enter the costumer's lastname.\n")
    while(CheckValidName(lastname)==False):
        lastname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        if(lastname=="0"):
            print("")
            Employee_menu()
            return
    email=input("Please enter the costumer's email.\n")
    while(CheckValidEmail(email)==False):
        email=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        if(email=="0"):
            print("")
            Employee_menu()
            return
    if(path.exists("Costumers/"+firstname+" "+lastname)==True):
        print("This costumer is already registered. Going back to the Employee menu")
        print("")
        Employee_menu()
        return
    else:
        os.mkdir("Costumers/"+firstname+" "+lastname)
        c=Costumer(firstname,lastname,email)
        details=open("Costumers/"+firstname+" "+lastname+"/"+firstname+" "+lastname+"-details.txt","w+")
        details.write(c.toString())
        details.close()
        savings=open("Costumers/"+firstname+" "+lastname+"/"+c.Accountnumber()+"-savings.txt","w+")
        savings.write(c.Savings().toString())
        savings.close()
        current=open("Costumers/"+firstname+" "+lastname+"/"+c.Accountnumber()+"-current.txt","w+")
        current.write(c.Savings().toString())
        current.close()
        print("Costumer account successfully created.")

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
                return
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
        CreateCostumerAccount()
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

def testdirectory():
    os.mkdir("example_directory/")
#testdirectory()

CreateCostumerAccount2()
#print(CheckValidName("Hervé-Henri"))
#print(CheckValidEmail("23857@student.dorset-college.ie"))
#main_menu()

