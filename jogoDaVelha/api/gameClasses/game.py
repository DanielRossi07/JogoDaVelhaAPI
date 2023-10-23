from .board import Board
from .player import Player, ComputerPlayer
from .pieceType import PieceType
from .gameLogic import GameLogic


class Game:
    player: Player
    computer: Player

    def __init__(self, player_name, player_type, socket):
        self.socket = socket
        self.board = Board()
        self.player = Player(player_name, player_type)
        self.computer = self.create_computer()
        self.game_logic = GameLogic(self.player, self.computer, self.board, self.socket)

    def create_computer(self):
        if self.player.pieceType == PieceType.x:
            computer_type = "O"
        else:
            computer_type = "X"

        return ComputerPlayer("Computer", computer_type)

    def make_a_move(self, row, col):
        self.game_logic.current_player.make_a_move(row, col)

    @staticmethod
    def validate_player_type(_input: str) -> str or None:
        options = "O0X"
        if _input not in options:
            return None
        return _input

    def end_game(self):
        self.game_logic.stop = True

