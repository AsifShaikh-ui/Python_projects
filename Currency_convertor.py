def ind_to_dol(currency):
    print(f"Your wallet after convertion : {round(currency/82.3,2)}")

def dol_to_ind(currency):
    print(f"Your wallet after convertion : {round((currency*82.3),2)}")

def main():
    print("\n-------Currency Converter--------")
    user = input("Enter the amount type Indian/Dollar (I/D): ").strip().lower()
    if user == "i":
        currency = int(input("Enter the amount: "))
        ind_to_dol(currency)
    elif user == "d":
        currency = int(input("Enter the amount: "))
        dol_to_ind(currency)
    else:
        print("Enter Valid Option")

if __name__ == "__main__":
    main()