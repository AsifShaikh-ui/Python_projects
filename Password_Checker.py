def log_in(user_name, password):
    user = input("Enter your user_name : ")
    pass_word = int(input("Enter the password: "))

    if user == user_name and  pass_word == password:
        print("Log In")
    else:
        print("User_name OR paasword Incorrect! ")

user_name = "xyzalpha"
password = 25807436

log_in(user_name, password)