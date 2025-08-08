
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, actual_answer, turns):
    """Check answer against guess, return the number of remaining turns."""
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it!!! The answer was {actual_answer}")
        return 0  # Return 0 to indicate the game is won

def set_difficulty():
    level = input("Choose difficulty 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100 :D")
    answer = randint(1, 100)
    
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You guessed it! Congratulations!")
            return
        
        if turns == 0:
            print("You're out of guesses. You lose!")
            return
        
        print("Guess again.")
        
game()
