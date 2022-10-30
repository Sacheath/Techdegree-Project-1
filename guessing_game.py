import random
from statistics import mode, median, mean

high_score = []

def start_game():
    if not high_score:
        print("Welcome to Team Treehouse's first project: Number Guessing Game!")
        print("\nThere's no current high score!")
    print("\nPick a number between 1 and 100!")

    while True:
        total_guesses = 0
        answer = random.randrange(1,100)

        while True:
            total_guesses += 1
            try:
                player_guess = int(input("> "))
                if player_guess <= 0 or player_guess > 100:
                    raise ValueError()
            except ValueError:
                print("That's not a valid guess. Please only use whole numbers between 1 and 100.")
                continue
            if player_guess > answer:
                print("It's lower!")
                continue
            elif player_guess < answer:
                print("It's higher!")
                continue
            else:
                print(f"You got it right in only {total_guesses} attempt(s)!")
                high_score.append(total_guesses)
                break

        while True:
            try:
                confirm_game = input("Do you want to play again?  > ")
                    
                if confirm_game.lower() == 'n':
                    print(f"""
                    Sorry to hear that. Here's your stats for this round!\n
                    Attempts: {total_guesses}
                    Mean Guess: {mean(high_score):.0f}
                    Median Guess: {median(high_score)}
                    Mode Guess: {mode(high_score)}\n
                    Come back later if you ever want to try again!""")
                    exit()
                elif confirm_game.lower() == 'y':
                    print(f"\nThe current high score is {min(high_score)} attempts!\n")
                    answer = random.randrange(1,100)
                    start_game()
                else:
                    raise ValueError()
            except ValueError:
                print("That's not a valid selection. Please enter either Y or N.")
                continue
start_game()