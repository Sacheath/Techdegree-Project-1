import random
from statistics import mode, median, mean

def start_game():
    print("Welcome to Team Treehouse's first project: Number Guessing Game!")
    
    answer = random.randrange(1,100)
    actual_guesses = []
    high_score = []  
    
    
    
    while True:
        try:
            confirm_game = input("Are you sure you want to give it a shot? Y/N: > ")
            if confirm_game.lower() == 'n':
                print("Sorry to hear that, have a nice day!")
                exit()
            if confirm_game.lower() == 'y':
                if len(high_score) < 1:
                    print("There is no current high score!")
                else:
                    print("The current high score is {} attempts!".format(min(high_score)))
                print("Pick a number between 1 and 100!")
                break
            else:
                raise ValueError()
        except ValueError:
            print("That's not a valid selection. Please enter either Y or N.")
            continue
    
    while True:
        try:
            player_guess = int(input("> "))
            if player_guess <= 0 or player_guess > 100:
                raise ValueError()
        except ValueError:
            print("That's not a valid guess. Please only use whole numbers between 1 and 100.")
            continue
            
        if player_guess > answer:
            print("It's lower!")
            actual_guesses.append(player_guess)
            continue
        elif player_guess < answer:
            print("It's higher!")
            actual_guesses.append(player_guess)
            continue
        else:
            print("You got it right in only {} attempts!".format(len(actual_guesses)))
            high_score.append(len(actual_guesses))
            break
    
    while True:
        try:
            restart = input ("How about another round? Y/N: > ")
            if restart.lower() == 'y':                
                print("Coming right up!")
                #how do I restart the game?
            if restart.lower() == 'n':
                print("""
        Sorry to hear that. Here's your stats for this round!
    
        Attempts: {}
        Mean Guess: {}
        Median Guess: {}
        Mode Guess: {}
    
        Come back later if you ever want to try again!
                """.format(total_guesses, round(mean(actual_guesses)), round(median(actual_guesses)), round(mode(actual_guesses))))
                exit()
            else:
                raise ValueError()
        except ValueError:
            print("Sorry that's not a valid selection. Please enter either Y or N.")

start_game()