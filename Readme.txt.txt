This file is a report on how we accomplished the project.

1. Our classes:
As you saw from our UML diagram we decided to create 4 different classes.
The Costumer, BankAccount, SavingsAccount and CurrentAccount classes.
We did not create a person class (with employee and costumers inheriting from it) as we judged it irrelevant 
for this project (simply because at no moment we are in need of an Employee object).
Although SavingsAccount and CurrentAccount do not have any specific code, we considered it relevant to seperate them
into two different objects for consistency purposes.
The attributes from the BankAccount class are protected since 2 other classes inherit from it.
The Costumer attributes are private.

2. The costumer database:
Since we are not working with a linked SQL database in this project, we had to find a way to store our costumers
somewhere without having to recreate all of them from file reading (which we found very tidious both for us to code
and for the machine to process).
We therefore decided to use the python pickle files.
All our costumers are saved into a list called CostumerList. 
Each time we perform a treatment on one of the costumers, it is automatically updated in the list (since the variable
is dynamic).
After each treatment, we save the list into a pickle file that we can retrieve later once we launch the program,
that way no file reading is needed to recreate a list of costumers.

3. Our general approach:
We decided to code almost all of our functions in the main py file (PythonCA.py), we could have seperated the 
methods into the different class files but we went for that option as we didn't have to constantly switch between tabs 
to compare or review code.

4. The challenges/struggles:
Working with Github wasn't difficult at all on our side.
We had troubles at first figuring out how to properly retrieve the costumer list before we found the pickle feature.
We found that finding, reading and writing files was the hardest part of the project as the methods remained 
quite simple.

Overall we enjoyed the project as we discovered the python language and managed to complete it without too much difficulty.
We found that this language is really the most optimised when it comes to file processing and it globally is a simple and 
optimised language pleaseant to code with.
