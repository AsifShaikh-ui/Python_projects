import random

def game():
    # 1 =r 2=p 3=s 
    print("Wlcome! to rock paper scissor game")
    print("r->rock\np->paper \ns->scissor")
    user=input("enter your choose: ")

    com = random.choice([1,2,3])
    my_dict = {1:"r",2:"p",3:"s"}
    computer = my_dict[com]
    rev_dict = {"r":"Rock","p":"Paper","s":"Scissor"}
    print(f"You choose: {rev_dict[user]} \nComputer choose: {rev_dict[computer]}")
    
    if(computer==user):
        print("It`s A Draw!")
    else:
        if(computer=="r" and user=="p"):
            print("You win!")
        elif(computer=="p" and user=="s"):
            print("You win!")
        elif(computer=="s" and user=="r"):
            print("You win!")   
        elif(computer=="r" and user=="s"):
            print("computer win!") 
        elif(computer=="s" and user=="p"):
            print("computer win!")
        elif(computer=="p" and user=="r"):
            print("computer win!")        


game()
