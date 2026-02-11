from config import (
    set_budget
    )

from database import (
    add_expense,
    create_table
    )

from reports import get_remaining_budget

from analytics import (
    get_monthly_total,
    get_category_summary,
    compare_month,
    get_last_n_month_totals,
    analyze_trend
    )


def main():

    create_table()

    while True:

        print("\n----------------Finance Manager---------------")
        print("""
1️⃣. Set Monthly Budget
2️⃣. Add Expense
3️⃣. View Remaining Budget
4️⃣. View Monthly Expense
5️⃣. Compare Monthly Spendings
6️⃣. See Trends Over N Months 
7️⃣. Exit
""")
        choice = input("Choose action from menu (1-7) : ")

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

        elif choice ==  "3":
            remaining = get_remaining_budget()

            print(f"\nRemaing budget : {remaining}")

            if remaining < 0 :
                print("Warning! You have exceeded your budget")
            else:
                print("Spendings is Undercontrol ")

        elif choice == "4":

            month = input("Enter the month (YYYY-MM): ")

            total = get_monthly_total(month)
            print(f"\nTotal expense for {month} : {total}")

            user = input("Want category wise summary (yes/no) : ").lower().strip()

            if user == "yes":
                summary = get_category_summary(month)
                if summary:
                    print("\n------------- Category Summary -------------\n")
                    for category, amount in summary:
                        print(f"{category} : {amount}")
                else:
                    print("Nothing to show")
        
        elif choice == "5":
            
            month = input("Enter the month (YYYY-MM): ")
            current_total = get_monthly_total(month)
            prev_total = compare_month(month)

            if prev_total == 0:
                print("NO data for previous month")
            elif current_total > prev_total : 
                print(f"Spendings increased by : {current_total - prev_total}")
            else:
                print(f"Good Job! Spending reduced by : {prev_total -  current_total}")

        elif choice == "6":
            month = input("Enter The month (YYYY-MM) : ")
            n = int(input("Number of months for trends : "))

            month_totals = get_last_n_month_totals(month, n)
            analysis = analyze_trend(month_totals)

            if analysis["trend"] == "Insufficient_Data":
                print("Not enough data to analyze trend.")
            else:
                print(f"Current : {analysis["current_total"]}")
                print(f"Previous : {analysis["previous_total"]}")
                print(f"Change : {analysis["change"]}")
                print(f"Trend : {analysis["trend"]}")


        elif choice == "7" :
            print("Goodbye...")
            break

        else:
            print("Please choose from menu only! ")


if __name__ == "__main__":
    main()
