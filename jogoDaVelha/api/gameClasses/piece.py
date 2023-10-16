from boardPosition import BoardPosition
from pieceType import PieceType


class Piece:
    def __init__(self, _type: PieceType, row: int, col: int):
        self.__position = BoardPosition(row, col)
        self.__type = _type

    @property
    def position(self):
        return self.__position

    @property
    def type(self):
        return self.__type

