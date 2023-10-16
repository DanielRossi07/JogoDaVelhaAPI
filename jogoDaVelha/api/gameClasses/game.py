from board import Board
from player import Player, ComputerPlayer
from pieceType import PieceType
from gameLogic import GameLogic


class Game:
    player: Player
    computer: Player

    def __init__(self):
        self.create_player()
        self.create_computer()
        self.board = Board()
        GameLogic(self.player, self.computer, self.board)

    def create_player(self):
        player_name = str(input("Digite seu nome: ")).capitalize()

        player_type = None
        while not player_type:
            player_type = str(input(f"{player_name}, qual peça você quer ser, 'X' ou 'O'? ")).upper()
            player_type = self.validate_player_type(player_type)

        print("\n\n")
        self.player = Player(player_name, player_type)

    def create_computer(self):
        if self.player.pieceType == PieceType.x:
            computer_type = "O"
        else:
            computer_type = "X"

        self.computer = ComputerPlayer("Computer", computer_type)

    @staticmethod
    def validate_player_type(_input: str) -> str or None:
        options = "O0X"
        if _input not in options:
            return None
        return _input


if __name__ == "__main__":
    game = Game()
