import random

words = ["hangman", "python", "programming", "computer", "science", "delhi", "india"]
word_to_guess = random.choice(words)

guessed_letters = []
attempts = 6
parts = [
                    "------",
                    "|    O",
                    "|   /|\\",
                    "|   / \\",
                    "|      ",
                    "---------"
                ]

print("Welcome to Hangman!")

while True:
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters or letter.lower() in guessed_letters:
            display += letter + " "
        elif letter.lower() in 'aeiou':
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    if "_" not in display:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess and guess not in 'aeiou':
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")


        print("\n".join(parts[attempts:]))

        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")
            break
    else:
        print("Please enter a valid single letter.")
