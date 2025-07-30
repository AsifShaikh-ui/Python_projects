import datetime as dt 

def add_Income():
    income=int(input("enter the addincome: "))
    total_income=income
    return total_income 

def expense_record():
    while(True):
        date = input("Please enter the date (YYYY-MM-DD): ")
        try:
            date_obj = dt.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")
            break
        type = input("Enter the mode of amount expense/Income : ")
        income = 0
        expense = 0
        if(type.lower() == "expense"):                
            expense = input("Enter Your expense amount: ")
        elif(type.lower() == "income"):     
            income = input("Enter Your income amount: ")
        else:
            print("Enter Right option")
            break  
        description = input("Enter the description of the amount: ")
        record_list = date + " | " + type + " | " + (expense or income) + " | " + description + "\n"
        with open("Expense_record.txt","a") as f:
            f.write(record_list)
        break

total_income=0
def show_menu():
    while(True):
        print("1.Add Income")
        print("2.Record Expense")
        print("3.view the balance")
        print("4.see transition history")
        print("5.Exit")
        user=int(input("enter option from the menu: "))
        if(user==1):
            total_income = add_Income()
        elif(user == 2):
           expense_record()
        elif(user==3):
            print(total_income) 
        elif(user==5):
            break       
show_menu()


