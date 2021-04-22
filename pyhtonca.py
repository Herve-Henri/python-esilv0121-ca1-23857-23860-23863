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




def main():
    menu()


main()