from game_logic import play_game

def main():
    while True:
        play_game()
        
        while True:
            choice = input("Do you want to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                break
            elif choice in ['n', 'no']:
                print("\nThanks for playing Snowman Meltdown! Goodbye!\n")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()
