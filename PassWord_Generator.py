import string
import random


def generate_password(length, user_up, user_low, user_dgt, user_symbol):

    if length > 8 and length < 15:

        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        special_symbols = string.punctuation

        char = ""

        if user_up:
            char += uppercase
        if user_low:
            char += lowercase
        if user_dgt:
            char += digits
        if user_symbol:
            char += special_symbols

        if not char:
            print("Error: No Char types selected")
        password = ""

        for _ in range(length):
            password += random.choice(char)

        print(f"Your new password is : {password}")
    else:
        print("Please Choose password length b/w 8-15")        
def main():
    user = input("Want to generate new password ? (y/n) : ").lower()
    if user == "y":

        print("\n-------Random Password Generator-------")
        length = int(input("Enter the lenght of password: ").strip())
        user_up = input("You want to add Upper_Case (y/n): ").lower() == "y"
        user_low = input("You want to add Lower_Case (y/n): ").lower() == "y"
        user_dgt = input("You want to add Digits (y/n): ").lower() == "y"
        user_symbol = input("You want to add Special_symbol (y/n): ").lower() == "y"

        generate_password(length, user_up, user_low, user_dgt, user_symbol)

    else:
        print("Thank you!")

if __name__ == "__main__":
    main()
