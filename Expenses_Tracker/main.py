from database import (
    create_table,
    add_expense,
    view_expense,
    delete_expense,
    get_total_expense,
    get_total_by_category
)

def main():

    create_table()

    while True:
        print("\n-------- Expense Tracker -------")
        print("1️⃣. Add Expenses \n2️⃣. View Expense Record \n3️⃣. Delete Expense \n4️⃣. View Total Expense \n5️⃣. Exit")

        choice = int(input("Choose from menu (1-4):  "))

        if choice == 1:

            amount = float(input("Enter the amount of expense : ")) 
            category = input("Enter Expense category: ")
            date = input("Enter the date of expense (YYYY-MM-DD): ")
            note = input("Enter the reason of expense: ")
            add_expense(amount, category, date, note)
            print("\nRecord Saved Successfully✅")

        elif choice == 2:

            expenses = view_expense()
            print("\n------------ All Expenses ------------\n")
            for ex in expenses:
                print(f"{ex[0]}. {ex[1]} | {ex[2]} | {ex[3]} | {ex[4]}")
        
        elif choice == 3:

            expenses = view_expense()
            print("\n------------ All Expenses ------------\n")
            for ex in expenses:
                print(f"{ex[0]}. {ex[1]} | {ex[2]} | {ex[3]} | {ex[4]}")

            expense_id = int(input("\nEnter the expense 'id' to delete : "))

            delete_expense(expense_id)
            print("\nOne Expense Deleted Successfully✅")
        
        elif choice == 4:
            total_expense = get_total_expense()
            print(f"\nTotal Expenses : {total_expense}")

            total_expense_by_category = get_total_by_category()
            print("\n------------ By Category --------------")
            for category, total in total_expense_by_category:
                print(f"{category} : {total}")


        elif choice ==  5:
            print("Done with Updation!")
            break
        else:
            print("Enter the choice in range!")

if __name__ == "__main__":
    main()