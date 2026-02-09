import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word progress."""
    # Clamp mistakes so we never index out of range
    mistakes = max(0, min(mistakes, len(STAGES) - 1))

    print(STAGES[mistakes])

    word_progress = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print("Word:", word_progress)
    print()


def get_valid_guess(guessed_letters):
    """Prompt the user until a single new alphabetical character is provided."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
        return guess


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = set()
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            mistakes += 1

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You guessed the word!")
            print("You saved the snowman!")
            break
    else:
        # This executes if the while loop finishes without a 'break'
        display_game_state(mistakes, secret_word, guessed_letters)
        print("Game Over! The snowman has melted.")
        print(f"The word was: {secret_word}")
        print("You failed to save the snowman.")
