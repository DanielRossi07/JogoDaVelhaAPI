from .board import Board
from .player import Player, ComputerPlayer
from .pieceType import PieceType
from .gameLogic import GameLogic


class Game:
    player: Player
    computer: Player

    def __init__(self):
        self.board = Board()

    def create_player(self, player_name: str, player_type: str, socket):
        self.player = Player(player_name, player_type, socket)

    def create_computer(self):
        if self.player.pieceType == PieceType.x:
            computer_type = "O"
        else:
            computer_type = "X"

        self.computer = ComputerPlayer("Computer", computer_type)

    def start(self):
        self.create_computer()
        GameLogic(self.player, self.computer, self.board)

    @staticmethod
    def validate_player_type(_input: str) -> str or None:
        options = "O0X"
        if _input not in options:
            return None
        return _input


if __name__ == "__main__":
    game = Game()
