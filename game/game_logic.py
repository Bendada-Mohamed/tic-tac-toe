from game.player import Player
from game.board import Board
from game.menu import Menu

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def setup_players(self):
        """Setup the players (name and symbol)"""
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details: ")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        """Main game loop"""
        while True:
            self.play_turn()
            if self.win_check() or self.draw_check():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        """Restart the game (reset board and start a new game)"""
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def play_turn(self):
        """Handle a single player's turn"""
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cellule = int(input("Choose cell (1-9): "))
                if 1 <= cellule <= 9 and self.board.update(cellule, player.symbol):
                    break
                print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        self.switch_player()

    def switch_player(self):
        """Switch the current player"""
        self.current_player_index = 1 - self.current_player_index

    def win_check(self):
        """Check if the current player has won"""
        win_possibilities = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]
        for combo in win_possibilities:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def draw_check(self):
        """Check if the game has ended in a draw"""
        return all(not cell.isdigit() for cell in self.board.board)

    @staticmethod
    def quit_game():
        """Display a quit message"""
        print("Thank you for playing!")

    def start_game(self):
        """Start the game by showing the menu"""
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()