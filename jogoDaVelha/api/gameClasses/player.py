from piece import Piece
from pieceType import PieceType
import random


class Player:
    def __init__(self, name: str, piece_type: str):
        self.name = name
        self.pieces = []
        self.pieceType = PieceType(piece_type)
        self.current_piece = None
        self.is_computer = False

    def play(self, row: int, col: int):
        self.validate_input(row, col)
        self.current_piece = Piece(self.pieceType, row, col)

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
        super().__init__(name, piece_type)
        self.is_computer = True

    def play(self):
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        self.current_piece = Piece(self.pieceType, row - 1, col - 1)