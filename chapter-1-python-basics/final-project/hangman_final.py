"""
This is one example of a finished version of the final project: Hangman.
"""

print("Welcome to hangman!")

secret_word = "secret"
guessed_word = ""

wrong_guesses = ""

# Infinite game loop that we eventually break out of
while True:
    # Start printing the hangman
    print("----")
    print("|  |")
    
    # Print the top part of the hangman
    # If the player has guessed wrong at least once, print the head.
    if len(wrong_guesses) > 0:
        print("|  O")

    # Otherwise, don't print the head.
    else:
        print("|   ")


    # Print the body of the hangman
    # If the player has guessed wrong twice, print the main body.
    if len(wrong_guesses) == 2:
        print("|  |")
    
    # Otherwise, if the player has guessed wrong 3 times, print the left arm too.
    elif len(wrong_guesses) == 3:
        print("| /|")

    # Otherwise, if the player has guessed wrong at least 4 times, print the right arm too.
    elif len(wrong_guesses) >= 4:
        # Remember that \ is an escape character. We need 2 of these in a row to print 1 backslash.
        print("| /|\\")

    # Otherwise, don't print any of the body parts.
    else:
        print("|   ")


    # Print the legs of the hangman
    # If the player has guessed wrong 5 times, print the left leg.
    if len(wrong_guesses) == 5:
        print("| /")
    
    
    # Otherwise, if the player has guessed wrong at least 6 times, print the right leg too.
    elif len(wrong_guesses) >= 6:
        print("| / \\")

    
    # Print the bottom of the structure
    print("|")
    print("----")

    print()

    # If the player has guessed wrong 6 times, break out of the game loop.
    if len(wrong_guesses) == 6:
        break

    # Print the guessed letters
    for character in secret_word:
        if character in guessed_word:
            print(character, end=" ")
        else:
            print("_", end=" ")
        
    print()

    
    # If the player has guessed all the letters, they win!
    is_correct = True
    for character in secret_word:
        if character not in guessed_word:
            is_correct = False
            break

    if is_correct:
        guessed_word = secret_word
        break


    # Get the next guess from the player
    guess = input("Guess a letter: ")
    # Convert to lowercase so that the game doesn't worry about case
    guess = guess.lower()

    # If the guess is more than one character, tell the player to guess only one letter at a time.
    if len(guess) > 1:
        print("Please guess only one letter at a time.")
        continue

    # If the player has already guessed the letter, tell them to guess again.
    if guess in guessed_word or guess in wrong_guesses:
        print("You have already guessed that letter.")
        continue

    # If the guess is in the secret word, add it to the guessed word
    if guess in secret_word:
        guessed_word += guess
    # Otherwise, add it to the wrong guesses
    else:
        wrong_guesses += guess


# If secret_word == guessed_word, the player won!
if secret_word == guessed_word:
    print("You win!")

# Otherwise, the player must have run out of guesses
else:
    print("You lose!")
    print("The word was:", secret_word)