import random

list_of_words = ['python','java','kotlin','javascript']

#TODO-1 - randomly choose a word from the list of words and assign it to a variable called chosen_word.

chosen_word = random.choice(list_of_words)
print(chosen_word)

#TODO-2 - ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.

guess = input("Guess a letter: ").lower()
print(guess)

#TODO-3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# print "Right" if it is, otherwise print "Wrong".
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
