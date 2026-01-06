expenses_list = [] #List of all Expences in dic 


print("WELCOME TO EXPENSE TRACKER ")
while True : 
    print('''======= OPERATION =======
      1)  Add Expense
      2) View All Expenses
      3) View Total Spending
      4) Exit''')
    print("=====================")

# OPTION 1
    choice = int (input("Enter your Choice: "))
    if (choice == 1) : 
        date = (input("Enter date (DD-MM-YYYY): "))
        category = (input("Enter category (Food, Travel, Shopping, etc): "))
        desc = (input("Enter short description:"))
        amount = float(input("Enter Amount: "))
        
        expense = {
            "date" : date , 
            "category" : category , 
            "desc" : desc , 
            "amount" : amount
        }
        expenses_list.append(expense)
        print("--- EXPENSE ADDED SUCESSFULLY ---")

# OPTION 2 VIEW ALL EXPENCES 
    elif choice ==  2 :
        if len(expenses_list) == 0 :
            print("No Previous Expence ")
        else:
            print("\n--- All Expenses ---")
        i = 1
        for e in expenses_list:
            print(f"{i}. {e['date']} | {e['category']} | {e['desc']} | ₹{e['amount']}")
            i += 1
            print("---------------------")

# OPTION 3 TOTAL SPENDING 
    elif (choice == 3) :
        total = 0
        for e in expenses_list :
            total = total + e ["amount"]
        print("\n TOTAL EXPENCES = ", total)

# OPTION 4 EXIT 
    elif choice == 4:
        print("\nThanks for using Expense Tracker! Bye!")
        break

    

    