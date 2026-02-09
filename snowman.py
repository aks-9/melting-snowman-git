import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
     """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
     """
]

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


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = set()

    # Partial implementation: just demonstrate stages increasing each loop
    while mistakes < len(STAGES):
        display_game_state(mistakes, secret_word, guessed_letters)
        input("Press Enter to advance to the next stage (testing): ")
        mistakes += 1


if __name__ == "__main__":
    play_game()