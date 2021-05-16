import random


def game(): 
    user_score = int(0)
    computer_score = int(0)
    user_limit = 2
    rounds = 1
    while rounds<3 and user_score != user_limit:
        user_action = int(input("Enter a choice\n1.rock\n2.paper\n3.scissors:\n"))
        possible_actions = [1, 2,3]
        computer_action = random.choice(possible_actions)
        
        print("You chose", user_action, "computer chose", computer_action)

        if user_action == computer_action:
            print("Both players selected",user_action, "It's a tie ")
            user_score=0
            computer_score =0
            print("User score",user_score)
            print("computer score: ",computer_score)   
        elif user_action == 1:
            if computer_action == 3 :
                print("Rock smashes scissors! You win!")
                user_score = user_score + 1
                print("User score",user_score)
                print("computer score: ",computer_score)
            else:
                print("Paper covers rock! You lose.")
                computer_score = computer_score + 1
                print("User score",user_score)
                print("computer score: ",computer_score)
        elif user_action == 2:
            if computer_action == 1 :
                print("Paper covers rock! You win!")
                user_score = user_score + 1
                print("User score",user_score)
                print("computer score: ",computer_score)
            else:
                print("Scissors cuts paper! You lose.")
                computer_score = computer_score + 1
                print("User score",user_score)
                print("computer score: ",computer_score)
        elif user_action == 3 :
            if computer_action == 2 :
                print("Scissors cuts paper! You win!")
                user_score = user_score + 1
                print("User score",user_score)
                print("computer score: ",computer_score)
            else:
                print("Rock smashes scissors! You lose.")
                computer_score = computer_score + 1
                print("User score",user_score)
                print("computer score: ",computer_score)
                if user_score == user_limit and rounds<3:
                    print("yay congrats u won")
                elif user_score == user_limit:
                    print("oopsies, the computer won, better luck next time")
                    break
      
         
game()
