def addincome():
    income=int(input("enter the addincome: "))
    total_income=income
    return total_income 





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
            total_income = addincome()
        elif(user==3):
            print(total_income) 
        elif(user==5):
            break       
show_menu()


