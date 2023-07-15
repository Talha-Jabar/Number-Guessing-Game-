import random

def inputs():
    print("Welcome to Number Guessing Game")
    # Taking inputs
    lower=int(input("Enter lower bound:- "))
    # Taking inputs
    upper=int(input("Enter upper bound:- "))
    # Generating random number between the lower and upper
    number=random.randint(lower,upper)
 

    # Initializing the number of tries
    tries=0

    # Asking for user name
    user_name=input("Enter your name: ")
    user_name=user_name.strip()
    print("hello!",user_name)

    # Asking the user to play or not
    print("Would you like to play a game?")
    print("1) Yes")
    print("2) No")

    # Asking the user to choose options
    option=int(input("Select your option: "))
    

    if option==1:
            print("I am thinking a number between",lower,"and",upper)
            print("You have to guess a number in five tries")
            # Taking guessing number as input
            guess=int(input("Guess a number: "))
            
            
            tries+=1
            
            # Condition Testing
            if guess>number:
                print("Please guess lower...")
            if guess<number:
                    print("Please guess higher...")
            while guess!=number and tries<5:
                guess=int(input("Try Again: "))
                
                tries+=1
                if guess>number:
                    print("Please guess lower...")
                if guess<number:
                    print("Please guess higher...")
            if guess==number:
                print("Congratulations,You won!")
                print("Number of tries:",tries)
                print("Would you like to play again?,press small 'y'for yes or small 'n' for not ")
                print("1) y")
                print("2) n")
                play_again=input("Enter your choice: ")
                if play_again=="y":
                    inputs()
                elif play_again=="n":
                    print("Thanks for playing")
            else:
                print("Oops,You lost!")
                print("The correct number was",number)
                print("Number of tries:",tries)
                print("Would you like to play again?,press small 'y'for yes or small 'n' for not ")
                print("1) y")
                print("2) n")
                play_again=input("Enter your choice: ")
                if play_again=="y":
                    inputs()
                elif play_again=="n":
                    print("Thanks for playing")
    elif option==2:
            print("As you wish")
    else:
            print("You have entered invalid option")

inputs()
