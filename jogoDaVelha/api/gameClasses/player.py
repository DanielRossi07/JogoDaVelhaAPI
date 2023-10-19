import json

from .piece import Piece
from .pieceType import PieceType
import random


class Player:
    def __init__(self, name: str, piece_type: str, socket):
        self.name = name
        self.pieces = []
        self.pieceType = PieceType(piece_type)
        self.current_piece = None
        self.is_computer = False
        self.socket = socket
        self.has_played = False

    def play(self):
        self.socket.send(text_data=json.dumps({
            'type': 'make_a_move'
        }))

    def make_a_move(self, row: int, col: int):
        self.validate_input(row, col)
        self.current_piece = Piece(self.pieceType, row, col)
        self.has_played = True

    @staticmethod
    def validate_input(row: int, col: int) -> bool:
        try:
            row = int(row)
            col = int(col)

            if 1 <= row <= 3 and 1 <= col <= 3:
                return True
            else:
                return False
        except ValueError:
            return False


class ComputerPlayer(Player):
    def __init__(self, name: str, piece_type: str):
        super().__init__(name, piece_type, None)
        self.is_computer = True

    def make_a_move(self, row=None, col=None):
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        self.current_piece = Piece(self.pieceType, row - 1, col - 1)
        self.has_played = True

    def play(self):
        self.make_a_move()
