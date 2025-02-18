class Player:
    used_symbols = set()
    player_count= 0
    def __init__(self):
        if Player.player_count >= 2:
            raise Exception("Only two players can be created")

        self.name = ""
        self.symbol = ""
        Player.player_count += 1

    def choose_name(self):
        while True:
            name = input("Enter your Name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, Please letters only!")
    def choose_symbol(self):
        while True:
            symbol = input(f"Hey {self.name}, Choose your symbol (One Letter): ").upper()
            if len(symbol) == 1 and symbol.isalpha() and symbol not in Player.used_symbols :
                self.symbol = symbol
                Player.used_symbols.add(symbol)
                break
            print("Invalid symbol, Please choose a single letter!")
class Menu:
    def display_main_menu(self):
        print("Welcome to my X-O game!")
        print("1. Strart Game")
        print("2. Quit Game")
        return self.validate_choice()
    def display_endgame_menu(self):
        print("""
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2):""")
        return self.validate_choice()
    @staticmethod
    def validate_choice():
        while True:
            try:
                choice = input("Enter your choice (1-2): ")
                if choice in ["1", "2"]:
                    return choice
                else:
                    print("Invalid choice, please choose 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (1 or 2).")
class Board:
    def __init__(self):
        self.board = [str(i) for i in range (1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)


    def update(self, cellule, symbol):
        if self.is_valid_move(cellule):
            self.board[cellule-1] = symbol
            return True
        return False


    def is_valid_move(self, cellule):
        return self.board[cellule-1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range (1,10)]
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f" Player {number}, enter your details: ")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.win_check():
                print(f"🎉 {self.players[self.current_player_index].name} wins the game! 🎉")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            elif self.draw_check():
                print("It's a draw! 🏳️")
                self.board.display_board()
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break



    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        print("Restarting the game...\n")
        self.play_game()
    def draw_check(self):
        return all(not cell.isdigit() for cell in self.board.board)
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cellule = int(input("choose cellule(1-9): ").strip())
                if 1 <= cellule <= 9:
                    if self.board.update(cellule, player.symbol):
                        break
                    else:
                        print("Cellule is already taken, try again.")
                else:
                    print("Invalid input! please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input, Please enter a number.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def win_check(self):
        win_possibilities = [
            [0,1,2], [3,4,5], [6,7,8], #rows
            [0,3,6],[1,4,7],[2,5,8], #columns
            [0,4,8],[2,4,6] #diagonal
        ]
        for combo in win_possibilities:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False


    @staticmethod
    def quit_game():
        print("Thank you for playing!")

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
game = Game()
game.start_game()