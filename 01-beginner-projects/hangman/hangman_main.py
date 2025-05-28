import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
all_guessed_letters = []  # Track ALL guessed letters (correct and incorrect) (Not included in Dr Angela Yu's code)

print(logo)

while not game_over:    # <-- THIS is the "top" ... where continue jumps back to

    guess = input("Guess a letter: ").lower()

    if guess in all_guessed_letters:
        print(f"You have already guessed '{guess}', Try a different letter") # Modified from original
        continue # continue is like a "skip button" inside a loop. When Python hits a continue statement,
        # it immediately jumps back to the beginning of the loop and starts the next iteration, skipping everything else in the current loop cycle.
        # aka "Skip everything below and ask for a new guess"

    # Add the guess to our list of all guessed letters
    all_guessed_letters.append(guess)

    display = ""

    # Game logic

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    ascii_art = f"****************************{lives}/6 LIVES LEFT****************************"

    if lives == 6:
        if not game_over:
            print(stages[6])
            print(ascii_art)
        else:
            print(chosen_word)
    elif 1 <= lives <= 5:
        print(stages[lives])
        print(ascii_art)
    else:
        print(stages[0])
        print(f"***********************YOU LOSE**********************\nThe mystery word was {chosen_word}")
