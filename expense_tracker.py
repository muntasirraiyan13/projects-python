#Expense Tracker Project

expenses=[]
while True:
    print("Menu:")
    print("1.Add an expense:")
    print("2.View all expenses:")
    print("3.Total expenses:")
    print("4.Delete an expense:")
    print("5.Clear all expenses:")
    print("6.Exit:")
    choice=int(input("Enter your choice:"))

    if (choice==1):
        date=input("Enter the date (YYYY-MM-DD):")
        category=input("Enter the category:")
        amount=float(input("Enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "amount":amount
        }
        expenses.append(expense)
        print("Expense added successfully!")

    elif (choice==2):
        if len(expenses)==0:
            print("No expenses recorded yet.")
        else:
            print("All Expenses:")
            count=1
            for expense in expenses:
                print(f"{count}. Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
                count+=1

    elif (choice==3):
        total=0
        for expense in expenses:
            total+=expense['amount']
        print(f"Total Expenses: ${total:.2f}")

    elif choice == 4:
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            item_num = int(input("Enter the expense number to delete: "))
            
            if 1 <= item_num <= len(expenses):
                removed_expense = expenses.pop(item_num - 1)
                print(f"Successfully deleted {removed_expense['category']} for ${removed_expense['amount']:.2f}")
            else:
                print("Invalid expense number.")

    elif (choice==5):
        if len(expenses) == 0:
            print("History is already empty.")
        else:
            confirm = input("Are you sure you want to delete ALL history? (y/n): ")
            if confirm.lower() == 'y':
                expenses.clear()
                print("All expense history has been deleted!")
            else:
                print("Deletion cancelled.")
    elif (choice==6):
        print("Exiting the Expense Tracker. Goodbye!")
        break
       
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

        


    
            

