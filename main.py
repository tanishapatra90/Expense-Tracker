# Expense Tracker Project

expenses = [] #list of all expenses in form of dictionary
print("Welcome to the Expense Tracker : Kharcha kam kiya karo")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    
    choice = int(input("Enter your choice :"))
    #ADD EXPENSE
    if(choice == 1):
        date = input("Enter the date of expense :")
        category = input("Enter the category of the expense:(Food, Travel, Makeup, Shopping, Books)")
        description = input("Enter the description of the expense:")
        amount = float(input("Enter the amount:"))
        
        expence = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expenses.append(expence)
        print(" \n Done bro. Expense added successfully!")
        
    #2. VIEW EXPENSES
    elif(choice == 2):
        if(len(expenses) == 0):
            print("No expences found. please add some expences first")
        else:
            print("========= YOUR EXPENSES=========")
            count = 1
            for expense in expenses:
                print(f"{count}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")
                count = count + 1
                
    #3. VIEW TOTAL EXPENSES
    elif(choice == 3):
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
            
        print("\n Total Expenses: ", total)
        
    #4. EXIT
    elif(choice == 4):
        print("Thank you for using the Expense Tracker ")
        print("Have a nice day !")
        break
    
    else:
        print("Invalid choice. Please try again.")
        
        
        
            
            
        
        
    
        