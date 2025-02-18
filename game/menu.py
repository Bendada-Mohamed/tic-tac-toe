class Menu:
    def display_main_menu(self):
        """Display the main menu"""
        print("Welcome to my X-O game!")
        print("1. Start Game")
        print("2. Quit Game")
        return self.validate_choice()

    def display_endgame_menu(self):
        """Display the endgame menu"""
        print("""
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2):""")
        return self.validate_choice()

    @staticmethod
    def validate_choice():
        """Validate the user's menu choice"""
        while True:
            try:
                choice = input("Enter your choice (1-2): ")
                if choice in ["1", "2"]:
                    return choice
                else:
                    print("Invalid choice, please choose 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (1 or 2).")
