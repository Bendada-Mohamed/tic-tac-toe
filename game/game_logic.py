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
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details: ")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            winner = self.win_check()
            if winner:
                self.switch_player()
                print(f"🎉 {self.players[self.current_player_index].name} wins the game! 🎉")
                self.board.display_board()
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
                cell = int(input("Choose a cell (1-9): ").strip())
                if 1 <= cell <= 9:
                    if self.board.update(cell, player.symbol):
                        break
                    else:
                        print("Cell is already taken, try again.")
                else:
                    print("Invalid input! Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def win_check(self):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in win_positions:
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