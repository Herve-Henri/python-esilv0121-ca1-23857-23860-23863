#23857 Hervé-Henri HOUZARD 
#23860 Ryan DOS SANTOS
#23863 Benjamin CONSTANT

def menu():
    print('****************Welcome to Dorset-Bank****************')
    print('***Please specify whether you are a user or employee**')
    choice=input("""
    
                  1:Costumer
                  2:Employee   
    """)
    if choice=="1":
        CostumerLogin()
    elif choice=="2":
        EmployeeLogin()
    else:
        print("You must enter either 1 or 2. \nPlease try again")
        menu()

def CostumerLogin():
    print("nothing for now")

def EmployeeLogin():
    print("nothing for now")

class Person:

    def __init__(self, firstname, lastname, email):
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
    
    def printname(self):
        print(self.firstname, self.lastname, self.email)

    def login_person(self):


class Employee(Person):
    def __init__(self, firstname, lastname, email):
        Person.__init__(self, firstname, lastname, email)
        #super().__init__(self, firstname, lastname, email) 
            #fonction qui fera en sorte que la classe enfant 
            #hérite de toutes les méthodes et propriétés de son parent
    
    def creation_customer(self):
    
    def deletion_customer(self):
    
    def saving_customer(self):

    def saving_account(self):
    
    def creation_transaction(self):
        #lodge
        #deposit
        def add_account(self):
        def withdraw_account(self):

    def show_customer(self):  
    
class Customer(Person):
    def __init__(self, firstname, lastname, email):
        Person.__init__(self, firstname, lastname, email)
        #super().__init__(self, firstname, lastname, email) 
            #fonction qui fera en sorte que la classe enfant 
            #hérite de toutes les méthodes et propriétés de son parent
    
    def retrieve_transaction(self):
    def add_money(self):
    def subtract_money(self):
    
   


def main():
    x = Employee("Ryan","DOS SANTOS","23860@student.dorset-college.ie")
    x.printname()
    menu()


main()