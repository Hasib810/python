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
list_of_words = ["python","java","cplusplus", "javascript","apple","banana","lambo","bahubali","imperial","ronaldo","realmadrid","siuu","hasib"]


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
    print(f"*****{lives}/6 Lives Left*****")

    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"you have already guessed the letter{guess}")
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



    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, thats not in the word, you lose life.")
    if lives == 0:
        game_over = True
        print(f"*****IT WAS {chosen_word} YOU LOSE!*****")
    
    if "_" not in  display:
        game_over = True
        print("*****YOU WIN!*****") 


print(stages[lives])