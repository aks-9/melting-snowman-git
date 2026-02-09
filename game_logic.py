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

    print("-" * 30)
    print(STAGES[mistakes])

    word_progress = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    
    print(f"Word: {word_progress}")
    
    # Display guessed letters in alphabetical order for readability
    if guessed_letters:
        print(f"Guessed: {', '.join(sorted(guessed_letters))}")
    else:
        print("Guessed: (None)")
    print("-" * 30)


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
    print("\n" + "=" * 30)
    print(" Welcome to Snowman Meltdown! ".center(30, "="))
    print("=" * 30 + "\n")

    mistakes = 0
    guessed_letters = set()
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"\n✅ Good job! '{guess}' is in the word.")
        else:
            print(f"\n❌ Sorry, '{guess}' is not in the word.")
            mistakes += 1

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("\n" + "*" * 30)
            print(" Congratulations! ".center(30, "*"))
            print(" You saved the snowman! ".center(30, "*"))
            print("*" * 30 + "\n")
            break
    else:
        # This executes if the while loop finishes without a 'break'
        display_game_state(mistakes, secret_word, guessed_letters)
        print("\n" + "!" * 30)
        print(" GAME OVER ".center(30, "!"))
        print(f" Word: {secret_word} ".center(30, "!"))
        print(" The snowman has melted. ".center(30, "!"))
        print("!" * 30 + "\n")
