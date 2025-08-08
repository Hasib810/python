import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |  
=========
''', '''
   +---+
   |   |
   O   |
       |
       |
       |  
=========
''', '''
   +---+
   |   |
       |
       | 
       | 
       | 
=========
''']
list_of_words = ["python","java","cplusplus", "javascript"]

#TODO-1 - create a variable called 'lives' to keep track of the number of the lives left.set 'lives' to 6.
lives = 6
chosen_word = random.choice(list_of_words)
print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:

    guess = input("Guess a letter: ").lower()
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
#TODO-2 - if guess is not the letter in the chosen_word, then reduce the 'lives' by1.
# if the 'lives' is 0, then print "you lose!" game is over.


    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        game_over = True
        print("you lose!")
    if "_" not in  display:
        game_over = True
        print("you win!") 

#TODO -3 - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
print(stages[lives])