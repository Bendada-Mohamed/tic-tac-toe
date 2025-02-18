class Player:
    used_symbols = set()
    player_count = 0

    def __init__(self):
        if Player.player_count >= 2:
            raise Exception("Only two players can be created")

        self.name = ""
        self.symbol = ""
        Player.player_count += 1

    def choose_name(self):
        """Allow the player to choose their name"""
        while True:
            name = input("Enter your Name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, Please letters only!")

    def choose_symbol(self):
        """Allow the player to choose a symbol (letter)"""
        while True:
            symbol = input(f"Hey {self.name}, Choose your symbol (One Letter): ").upper()
            if len(symbol) == 1 and symbol.isalpha() and symbol not in Player.used_symbols:
                self.symbol = symbol
                Player.used_symbols.add(symbol)
                break
            print("Invalid symbol, Please choose a single letter!")
