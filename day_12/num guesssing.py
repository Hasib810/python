from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, actual_answer, turns):
    """check answer against guess, returns the number of remaining"""

    if user_guess > actual_answer:
        print("too high!")
        return turns-1
    elif user_guess < actual_answer:
        print("too low!")
        return turns-1
    else:
        print("you got it!!!, the answer was {actual_answer}")


def set_difficulty():
    level = input("choose difficulty 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("welcome to number guessing game!")
    print("im thinking number between 1 to 100 :D")
    answer = randint(1, 100)


    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"you have {turns} attemps to guess remainig")
        guess = int(input("make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("you are run out of guesses, you lose")
        return
    elif guess!= answer:
        print("guess again")
game()