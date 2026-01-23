def checker(user):

    copy = user[::-1]

    if user == copy:
        print("It`s a palindrome ")
    else:
        print("It`s not a palindrome")

def main():
    print("\n-------Palindrome Checker-------")
    user = input("Enter the sentence/number to check : ")
    checker(user)

if __name__ == "__main__":
    main()