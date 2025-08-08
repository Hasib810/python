import random
list_of_words = ["python","java","cplusplus", "javascript"]
chosen_word = random.choice(list_of_words)
print(chosen_word)

#TODO-1 - create a "placeholder" with the same number of blanks as the chosen_word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()

#TODO-2 - create a "display" that puts the guessed letter in the correct postion in the placeholder and _ for the rest.

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
