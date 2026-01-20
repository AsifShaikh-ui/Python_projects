import random


def player_1():
    player1_score  = 0
    while True:
        

        score  = random.randint(0,6)

        if score == 0:
            print(f" {score} --> OUT!")
            return player1_score
            
        else:
            print(f"You hit --> {score}")
            player1_score += score 
        

def player_2():
    player2_score  = 0
    while True:
        
        score  = random.randint(0,6)

        if score == 0:
            print(f" You hit {score} --> OUT!")
            return player2_score
        else:
            print(f"You hit --> {score}")
            player2_score += score 



def main():
    print("--------Let`s play--------")
    print("Fisrt Player starts")
    first_score  = player_1()
    print(f"Total Score : {first_score}")
    print("\nSecond Player Starts ")
    second_score = player_2()
    print(f"Total Score : {second_score}")

    if first_score > second_score:
        print("\n Fisrt player Wins")
    else:
        print("\n Scond Player Wins ")


    
if __name__ == "__main__":
    main()