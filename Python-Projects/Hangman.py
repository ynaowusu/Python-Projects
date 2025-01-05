
import random
from hangman_words import word_list
from hangman_art import stages, logo



print(logo)


lives = 6 
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position  in range(word_length):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letters = []
 
while not game_over:
    print(f"******************* You have {lives}/ 6 LIVES LEFT ****************** ")
    guess = input("Guess a letter: ")
    guess = guess.lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
 

    display = ""


    for letter in chosen_word:
    
        if guess == letter:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"**************THE WORD WAS : {chosen_word.upper()} YOU LOSE ******************")

    if "_" not in display:
        game_over = True
        print("You win")
    

    print(stages[lives])


