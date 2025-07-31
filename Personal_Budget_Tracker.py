import datetime as dt 
total_income = 0

def add_Income():
    income=int(input("enter the addincome: "))
    total_income=income
    return total_income 


def expense_record():
    global total_income
    income=0
    expense=0
    while(True):
        date = input("Please enter the date (YYYY-MM-DD): ")
        try:
            date_obj = dt.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")
            break
        type = input("Enter the mode of amount expense/Income : ")
        if(type.lower() == "expense"):                
            expense = input("Enter Your expense amount: ")
        elif(type.lower() == "income"):     
            income = input("Enter Your income amount: ")
        else:
            print("Enter Right option")
            break  
        description = input("Enter the description of the amount: ")
        record_list = date + " | " + type + " | " + (expense or income) + " | " + description + "\n"
        total_income = total_income-int(expense)
        total_income = total_income+int(income)
        with open("Expense_record.txt","a") as f:
            f.write(record_list)
        break
    return total_income

def record():
    with open("Expense_record.txt") as f:
        print("...............Your Transaction history/.........................")
        print(f.read())


income = 0
expense = 0
def show_menu():
    while(True):
        print("1.Add Income")
        print("2.Record Expense")
        print("3.view the balance")
        print("4.see transition history")
        print("5.Exit")
        user=int(input("enter option from the menu: "))
        if(user==1):
            global total_income
            total_income = add_Income()
        elif(user == 2):
           a = expense_record()
           total_income = a
        elif(user==3):
            print(f"Your wallet after all transaction: {total_income}")
        elif(user==4):
            record()
        elif(user==5):
            break       
show_menu()


