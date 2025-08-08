import random
list_of_words = ["python","java","cplusplus", "javascript"]
chosen_word = random.choice(list_of_words)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#TODO-1 - use a while loop to let the user guess again.
game_over = False
correct_letters = []
while not game_over:

    guess = input("Guess a letter: ").lower()
    display = ""

    #TODO-2 - change the for loop so that you keep the previous correct


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if "_" not in  display:
        game_over = True
        print("you win!") 
