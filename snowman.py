from game_logic import play_game


def main():
    """Main entry point for the Snowman Meltdown game."""
    while True:
        play_game()

        while True:
            prompt = "Do you want to play again? (y/n): "
            choice = input(prompt).lower().strip()
            if choice in ['y', 'yes']:
                break
            if choice in ['n', 'no']:
                print("\nThanks for playing Snowman Meltdown! Goodbye!\n")
                return

            print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
