from database import (
    create_table,
    add_expense
)

def main():

    create_table()

    while True:
        print("\n-------- Expense Tracker -------")
        print("1. Add Expenses \n2. View Expense Record \n3. Delete Expense \n4.Exit")

        choice = int(input("Choose from menu (1-4):  "))

        if choice == 1:

            amount = float(input("Enter the amount of expense : ")) 
            category = input("Enter Expense category: ")
            date = input("Enter the date of expense (YYYY-MM-DD): ")
            note = input("Enter the reason of expense: ")
            add_expense(amount, category, date, note)
            print("Record Saved successfully")

        elif choice ==  4:
            print("Done with updation!")
            break
        else:
            print("Enter the choice in range!")

if __name__ == "__main__":
    main()