import time
import random

def math_challenge():
    operator = ["+","-","*","/"]
    start_time = time.time()
    count = 0
    print("You have 1 min! \nGood Luck")
    while time.time() - start_time <=60:
        
        fisrt_vaiable = random.randint(1,20)
        second_variable = random.randint(1,20)
        ops = random.choice(operator)
        if ops == "/":
            b_op_a = "{} {} {}".format(second_variable, ops, fisrt_vaiable)
            ans = int(eval(b_op_a))
        else:    
            a_op_b = "{} {} {}".format(fisrt_vaiable, ops, second_variable)
            ans = int(eval(a_op_b))
        print(f"Remaining {int(60 - (time.time() - start_time))} seconds")
        user_answer = int(input(f"{fisrt_vaiable} {ops} {second_variable} : "))

        if user_answer == ans:
            count += 1
            print("You got it right!")
        else:
            print("sorry! It wrong")

    print(f"You have got total {count} right answer")

def player():
    print("------welcome to math challenge------")
    permission = input("Should we start (yes/no) : ").strip().lower()

    if permission == "yes":
        math_challenge()
    else:
        print("Thank You!")

player()
