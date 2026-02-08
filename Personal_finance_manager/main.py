from config import (
    set_budget
    )

from database import (
    add_expense,
    create_table
    )

from reports import get_remaining_budget
from analytics import get_monthly_total


def main():

    create_table()

    while True:

        print("\n----------------Finance Manager---------------")
        print("1️⃣. Set Monthly Budget \n2️⃣. Add Expense \n3️⃣. View Remaining budget \n4️⃣. View Monthly Expense \n5️⃣. Exit")

        choice = input("Choose action from menu (1-5) : ")

        if choice == "1":

            try:
                amount = float(input("\nEnter this month budget: "))
            except ValueError:
                print("Invalid amount")
                continue
            
            if set_budget(amount):
                print("This month budget set successfully ")
            else:
                print("Budget Should be > 0 ")

        elif choice == "2" :
            try:
                amount = float(input("Enter the expense amount: "))
            except ValueError:
                print("Invalid Input")
                continue
            category = input("Enter the category of expense: ")
            date = input("Enter the date of expense (YYYY-MM-DD) : ")
            note = input("note for expense: ")

            if add_expense(amount, category, date, note):
                print("Expense recorded successfully!")
            else:
                print("Failed to record expense")

        elif choice ==  "3 ":
            remaining = get_remaining_budget()

            print(f"\n{remaining}")

            if remaining < 0 :
                print("Warning! You have exceeded your budget")
            else:
                print("Spendings is Undercontrol ")

        elif choice == "4":

            month = input("Enter the month (YYYY-MM): ")

            total = get_monthly_total(month)
            print(f"Total expense for {month} : {total}")

        elif choice == "5" :
            print("Goodbye...")
            break

        else:
            print("Please choose from menu only! ")


if __name__ == "__main__":
    main()
