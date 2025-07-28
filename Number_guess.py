import random
def guess_number():
    num=random.randint(1,100)
    count = 0
    while(True):
        user=int(input("enter the number between 1 to 100 : "))
        if(user>num):
            print("Lower Number Please!")
            count +=1
        elif(user<num):
            print("Higher Number Please!") 
            count +=1 
        elif(user==num):
            print("Congrats! You guess the right number!")
            count += 1
            break
    print(f"You guess the number \'{num}\' in \'{count}\' guess")
    
guess_number()
 