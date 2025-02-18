class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]  # Initialize board with numbers 1-9

    def display_board(self):
        """Display the current state of the game board"""
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)

    def update(self, cellule, symbol):
        """Update the board with player's symbol"""
        if self.is_valid_move(cellule):
            self.board[cellule - 1] = symbol
            return True
        return False

    def is_valid_move(self, cellule):
        """Check if the move is valid (cell is still a number)"""
        return self.board[cellule - 1].isdigit()

    def reset_board(self):
        """Reset the board to its initial state"""
        self.board = [str(i) for i in range(1, 10)]