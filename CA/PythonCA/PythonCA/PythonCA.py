from Costumer import Costumer
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from BankAccount import BankAccount
from datetime import datetime
import os, glob
import shutil
import pickle
from os import path

#Loading/creating our dynamic costumer database first
if path.exists('costumers.pkl'):
    with open('costumers.pkl','rb') as f:
            CostumerList = pickle.load(f)
else:
    CostumerList = []

def savecostumerDB():
    with open('costumers.pkl','wb') as f:
        pickle.dump(CostumerList, f)

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

def CostumerCreation(firstname,lastname,email):
    os.mkdir("Costumers/"+firstname+" "+lastname)
    c=Costumer(firstname,lastname,email)
    CostumerList.append(c)
    savecostumerDB()
    details=open("Costumers/"+firstname+" "+lastname+"/"+firstname+" "+lastname+"-details.txt","w+")
    details.write(c.toString())
    details.close()
    savings=open("Costumers/"+firstname+" "+lastname+"/"+c.Accountnumber()+"-savings.txt","w+")
    savings.write(c.Savings().toString())
    savings.close()
    current=open("Costumers/"+firstname+" "+lastname+"/"+c.Accountnumber()+"-current.txt","w+")
    current.write(c.Current().toString())
    current.close()
    transactions=open("Costumers/"+firstname+" "+lastname+"/"+c.Accountnumber()+"-transactions.txt","w+")
    transactions.close()

def CreateCostumerAccount():
    firstname=input("Please enter the costumer's firstname.\n")
    firstname=firstname.lower()
    while(CheckValidName(firstname)==False):
        firstname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        firstname=firstname.lower()
        if(firstname=="0"):
            print("")
            Employee_menu()
            return
    lastname=input("Please enter the costumer's lastname.\n")
    lastname=lastname.lower()
    while(CheckValidName(lastname)==False):
        lastname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        lastname=lastname.lower()
        if(lastname=="0"):
            print("")
            Employee_menu()
            return
    email=input("Please enter the costumer's email.\n")
    while(CheckValidEmail(email)==False):
        email=input("This email is not valid, please enter a valid email.\n(Or enter 0 to go back to the Employee menu.)\n")
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
        CostumerCreation(firstname,lastname,email)
        print("Costumer account successfully created. Going back to the Employee menu")
        print("")
        Employee_menu()

def CostumerDeletion(firstname,lastname):
    for Costumer in CostumerList:
            if(Costumer.Firstname()==firstname and Costumer.Lastname()==lastname):
                shutil.rmtree("Costumers/"+firstname+" "+lastname)
                CostumerList.remove(Costumer)
                savecostumerDB()

def DeleteCostumerAccount():
    firstname=input("Please enter the costumer's firstname.\n")
    firstname=firstname.lower()
    while(CheckValidName(firstname)==False):
        firstname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        firstname=firstname.lower()
        if(firstname=="0"):
            print("")
            Employee_menu()
            return
    lastname=input("Please enter the costumer's lastname.\n")
    lastname=lastname.lower()
    while(CheckValidName(lastname)==False):
        lastname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        lastname=lastname.lower()
        if(lastname=="0"):
            print("")
            Employee_menu()
            return
    if(path.exists("Costumers/"+firstname+" "+lastname)==False):
        print("This costumer is not registered. Going back to the Employee menu")
        print("")
        Employee_menu()
        return
    else:
        for Costumer in CostumerList:
            if(Costumer.Firstname()==firstname and Costumer.Lastname()==lastname):
                if(Costumer.Savings().Balance()==0.00 and Costumer.Current().Balance()==0.00):
                    shutil.rmtree("Costumers/"+firstname+" "+lastname)
                    CostumerList.remove(Costumer)
                    savecostumerDB()
                    print("The costumer "+firstname+" "+lastname+" was successfully deleted.\nGoing back to the Employee menu")
                    print("")
                    Employee_menu()
                    return
                else:
                    print("Cannot delete that costumer, check their account balances.\nGoing back to the Employee menu")
                    print("")
                    Employee_menu()
                    return

def GetSavingAccountHistory():
    for Costumer in CostumerList:
        print("savings:"+str(Costumer.Savings().Balance()))
    print("")
    Costumer_menu()

def GetCurrentAccountHistory():
    for Costumer in CostumerList:
        print("current:"+ str(Costumer.Current().Balance()))
    print("")
    Costumer_menu()

def GetCostumerList():
    for Costumer in CostumerList:
        print(Costumer.Firstname()+" "+Costumer.Lastname()+"  account number:"+Costumer.Accountnumber()+"  current:"
              + str(Costumer.Current().Balance())+ "  savings:"+str(Costumer.Savings().Balance()))
    print("")
    Employee_menu()

def Employee_login():
    #extra anti brute force measure (made for fun)
    n=0
    print("Please enter the login password:")
    choice=input("")
    if choice=="A1234":
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

def ChangeBalance(costumer):
    choice=input("What do you wish to do?"
                +"\n1:Change the current account's balance."
                +"\n2:Change the savings account's balance. \n")
    while(choice!="1" and choice!="2"):
        choice=input("You must enter either 1, 2 or 0 if you wish to go back to the employee menu.\n")
        if(choice=="0"):
            print("")
            Employee_menu()
            return
    if choice=="1":
        choice2=input("What action do you wish to do?"
                     +"\n1:Add money to that account."
                     +"\n2:Withdraw money from that account.\n")
        while(choice2!="1" and choice2!="2"):
            choice2=input("You must enter either 1, 2 or 0 if you wish to go back to the employee menu.\n")
            if(choice2=="0"):
                print("")
                Employee_menu()
                return
        if choice2=="1":
            amount=float(input("Please enter the amount you wish to add: "))
            while(amount < 0):
                amount=float(input("You cannot add a negative amount, please enter a positive amount. (or enter 0 to go back to the Employee menu).\n"))
                if(amount==0.0):
                    print("")
                    Employee_menu()
                    return                 
            amount=round(amount,2)
            costumer.Current().Add(amount)
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-current.txt","r") as cfile:
                data=cfile.readlines()
            data[0]=costumer.Current().toString()+"\n"
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-current.txt","w") as cfile:
                cfile.writelines(data)
                cfile.write("\n"+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" +"+str(amount)+"€  ->"+str(costumer.Current().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","r") as tfile:
                data=tfile.readlines()
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","w") as tfile:
                tfile.writelines(data)
                tfile.write("\n"+costumer.Current().Name()+" "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" +"+str(amount)+"€  ->"+str(costumer.Current().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Firstname()+" "+costumer.Lastname()+"-details.txt","w") as details:
                details.write(costumer.toString())
            savecostumerDB()
            print("Succesfully added "+str(amount)+"€ to that account. Going back to the Employee menu. \n")
            Employee_menu()
            return
        if choice2=="2":
            amount=float(input("Please enter the amount you wish to withdraw: "))
            while(amount>costumer.Current().Balance()):
                print("The balance cannot be negative, please withdraw a lower amount (or enter 0 to go back to the Employee menu).\n")
                amount=float(input(""))
                if(amount==0.0):
                    print("")
                    Employee_menu()
                    return
            amount=round(amount,2)
            costumer.Current().Withdraw(amount)
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-current.txt","r") as cfile:
                data=cfile.readlines()
            data[0]=costumer.Current().toString()+"\n"
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-current.txt","w") as cfile:
                cfile.writelines(data)
                cfile.write("\n"+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" -"+str(amount)+"€  ->"+str(costumer.Current().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","r") as tfile:
                data=tfile.readlines()
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","w") as tfile:
                tfile.writelines(data)
                tfile.write("\n"+costumer.Current().Name()+" "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" -"+str(amount)+"€  ->"+str(costumer.Current().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Firstname()+" "+costumer.Lastname()+"-details.txt","w") as details:
                details.write(costumer.toString())
            savecostumerDB()
            print("Succesfully withdrew "+str(amount)+"€ from that account. Going back to the Employee menu. \n")
            Employee_menu()
    if choice=="2":
        choice2=input("What action do you wish to do?"
                     +"\n1:Add money to that account."
                     +"\n2:Withdraw money from that account. \n")
        while(choice2!="1" and choice2!="2"):
            choice=input("You must enter either 1, 2 or 0 if you wish to go back to the employee menu. \n")
            if(choice=="0"):
                print("")
                Employee_menu()
                return
        if choice2=="1":
            amount=float(input("Please enter the amount you wish to add: "))
            while(amount < 0):
                amount=float(input("You cannot add a negative amount, please enter a positive amount. (or enter 0 to go back to the Employee menu).\n"))
                if(amount==0.0):
                    print("")
                    Employee_menu()
                    return                 
            amount=round(amount,2)
            costumer.Savings().Add(amount)
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-savings.txt","r") as cfile:
                data=cfile.readlines()
            data[0]=costumer.Savings().toString()+"\n"
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-savings.txt","w") as cfile:
                cfile.writelines(data)
                cfile.write("\n"+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" +"+str(amount)+"€  ->"+str(costumer.Savings().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","r") as tfile:
                data=tfile.readlines()
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","w") as tfile:
                tfile.writelines(data)
                tfile.write("\n"+costumer.Savings().Name()+" "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" +"+str(amount)+"€  ->"+str(costumer.Savings().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Firstname()+" "+costumer.Lastname()+"-details.txt","w") as details:
                details.write(costumer.toString())
            savecostumerDB()
            print("Succesfully added "+str(amount)+"€ to that account. Going back to the Employee menu. \n")
            Employee_menu()
            return
        if choice2=="2":
            amount=float(input("Please enter the amount you wish to withdraw: "))
            while(amount>costumer.Savings().Balance()):
                print("The balance cannot be negative, please withdraw a lower amount (or enter 0 to go back to the Employee menu).\n")
                amount=float(input(""))
                if(amount==0.0):
                    print("")
                    Employee_menu()
                    return
            amount=round(amount,2)
            costumer.Savings().Withdraw(amount)
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-savings.txt","r") as cfile:
                data=cfile.readlines()
            data[0]=costumer.Savings().toString()+"\n"
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-savings.txt","w") as cfile:
                cfile.writelines(data)
                cfile.write("\n"+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" -"+str(amount)+"€  ->"+str(costumer.Savings().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","r") as tfile:
                data=tfile.readlines()
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Accountnumber()+"-transactions.txt","w") as tfile:
                tfile.writelines(data)
                tfile.write("\n"+costumer.Savings().Name()+" "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" -"+str(amount)+"€  ->"+str(costumer.Savings().Balance())+"€")
            with open("Costumers/"+costumer.Firstname()+" "+costumer.Lastname()+"/"+costumer.Firstname()+" "+costumer.Lastname()+"-details.txt","w") as details:
                details.write(costumer.toString())
            savecostumerDB()
            print("Succesfully withdrew "+str(amount)+"€ from that account. Going back to the Employee menu. \n")
            Employee_menu()
   
def ChangeAccountBalance():
    firstname=input("Please enter the costumer's firstname.\n")
    firstname=firstname.lower()
    while(CheckValidName(firstname)==False):
        firstname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        firstname=firstname.lower()
        if(firstname=="0"):
            print("")
            Employee_menu()
            return
    lastname=input("Please enter the costumer's lastname.\n")
    lastname=lastname.lower()
    while(CheckValidName(lastname)==False):
        lastname=input("This name is not valid, please enter a valid name.\n(Or enter 0 to go back to the Employee menu.)\n")
        lastname=lastname.lower()
        if(lastname=="0"):
            print("")
            Employee_menu()
            return
    if(path.exists("Costumers/"+firstname+" "+lastname)==False):
        print("This costumer is not registered. Going back to the Employee menu")
        print("")
        Employee_menu()
        return
    else:
        for Costumer in CostumerList:
            if(Costumer.Firstname()==firstname and Costumer.Lastname()==lastname):
                ChangeBalance(Costumer)

def Employee_menu():
    choice=input("What action do you wish to do:"
               +"\n 1:Create a new costumer account"
               +"\n 2:Delete a costumer account"
               +"\n 3:Get the costumer list"
               +"\n 4:Change a costumer's bank account balance"
               +"\n 5:Log out\n")
    if choice=="1":
        CreateCostumerAccount()
    elif choice=="2":
        DeleteCostumerAccount()
    elif(choice=="3"):
        GetCostumerList()
    elif(choice=="4"):
        ChangeAccountBalance()
    elif(choice=="5"):
        print("Going back to the main menu\n")
        main_menu()
    else:
         print("You must enter a digit between 1 and 5 \nPlease try again")
         Employee_menu()

def Costumer_menu():
    choice=input("What action do you wish to do:"
               +"\n 1:Get the transaction history"
               +"\n 2:Add money to your account"
               +"\n 3:Withdraw from your account"              
               +"\n 4:Log out\n")
    while(choice!="1" and choice!="2" and choice!="3" and choice!="4"):
        choice=input("You must enter either 1, 2, 3, 4 or 0 if you wish to go back to the menu.\n")
        if(choice=="0"):
            print("")
            main_menu()
            return
    if choice=="1":
         choice1=input("What do you wish to do?"
                +"\n1:Get from the current account's balance."
                +"\n2:Get from the savings account's balance. \n")
         while(choice1!="1" and choice1!="2"):
            choice1=input("You must enter either 1, 2 or 0 if you wish to go back to the costumer menu.\n")
            if(choice1=="0"):
                print("")
                Costumer_menu()
            elif(choice1=='1'):
                GetSavingAccountHistory()
            elif(choice1=='2'):
                GetCurrentAccountHistory()
            else:
                choice1=input("What do you wish to do?"
                +"\n1:Get from the current account's balance."
                +"\n2:Get from the savings account's balance. \n")
            return
    elif choice=="2":
        choice2=input("What do you wish to do?"
                +"\n1:Add money to the current account."
                +"\n2:Add money to the savings account. \n")
        while(choice2!="1" and choice2!="2"):
            choice2=input("You must enter either 1, 2 or 0 if you wish to go back to the costumer menu.\n")
            if(choice2=="0"):
                print("")
                Costumer_menu()
            elif(choice2=="1"):
                ############
            elif(choice2=="2"):
                ############
            else:
                choice2=input("What do you wish to do?"
                +"\n1:Add money to the current account."
                +"\n2:Add money to the savings account. \n")
    elif(choice=="3"):
        choice3=input("What do you wish to do?"
                +"\n1:Withdraw money from the current account."
                +"\n2:Withdraw money from the savings account. \n")
        while(choice3!="1" and choice3!="2"):
            choice3=input("You must enter either 1, 2 or 0 if you wish to go back to the costumer menu.\n")
            if(choice3=="0"):
                print("")
                Costumer_menu()
            elif(choice3=="1"):
                ############
            elif(choice3=="2"):
                ############
            else:
                choice3=input("What do you wish to do?"
                +"\n1:Withdraw money from the current account."
                +"\n2:Withdraw money from the savings account. \n")
    elif(choice=="4"):
      print("Going back to the main menu\n")
      main_menu()
    else:
         print("You must enter a digit between 1 and 4 \nPlease try again")
         Customer_menu()

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

def pickletest():
    for Costumer in CostumerList:
        print(Costumer.toString())

def datetimetest():
    now=datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(now)
    print(dt_string)

def btest():
    for Costumer in CostumerList:
        if (Costumer.Firstname()=="larry" and Costumer.Lastname()=="hogard"):
                print(Costumer.toString())
                ChangeBalance(Costumer)


def readlinetest():
    with open("test.txt","r") as file:
        data=file.readlines()
    data[0]="Nada\n"
    with open("test.txt","w") as file:
        file.writelines(data)
        file.write("\nextra")
#print(CheckValidName("Hervé-Henri"))
#print(CheckValidEmail("23857@student.dorset-college.ie"))
#pickletest()
#datetimetest()
#readlinetest()
#btest()
main_menu()




