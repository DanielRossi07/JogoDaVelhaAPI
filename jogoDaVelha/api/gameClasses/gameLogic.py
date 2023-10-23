import json
import time

from .board import Board
from .player import Player
from random import randint


class GameLogic:
    current_player = None
    winner = False
    tie = False
    game_over = False
    end_type = None

    def __init__(self, player1: Player, player2: Player, game_board: Board):
        self.player1 = player1
        self.player2 = player2
        self.game_board = game_board
        self.start()

    def start(self):
        self.draw_player()

    def play(self):
        print("Choosing first player")

        self.next_player()

        if self.current_player.is_computer:
            self.current_player.play()

        if not self.register_play():
            if self.current_player.is_computer:
                while not self.register_play():
                    self.current_player.play()
            else:
                self.current_player.play()
                self.current_player.valid_move = False
                return self.get_gamestatus()

        self.verify_if_winner_or_tie()

        if self.winner:
            self.end_type = 'win'
            self.game_over = True
        if self.tie:
            self.end_type = 'tie'
            self.game_over = True

        return self.get_gamestatus()

    def draw_player(self):
        number = randint(0, 1)
        if number == 0:
            self.current_player = self.player1
        else:
            self.current_player = self.player2

    def next_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def verify_if_winner_or_tie(self):
        self.verify_win_by_rows()
        self.verify_win_by_columns()
        self.verify_win_by_diagonal()
        self.verify_if_tie()

    def verify_win_by_rows(self):
        rows = self.game_board.rows

        for row in rows:
            first_piece_of_row = row[0]
            if self.game_board.is_default_piece(first_piece_of_row):
                break

            row_winner = all(piece.type == first_piece_of_row.type for piece in row)

            if row_winner:
                self.winner = self.current_player

    def verify_win_by_columns(self):
        cols = self.game_board.columns

        for col in cols:
            first_piece_of_col = col[0]
            if self.game_board.is_default_piece(first_piece_of_col):
                break

            col_winner = all(piece.type == first_piece_of_col.type for piece in col)

            if col_winner:
                self.winner = self.current_player

    def verify_win_by_diagonal(self):
        diagonals = self.game_board.diagonals

        for diagonal in diagonals:
            first_piece_of_diagonals = diagonal[0]
            if self.game_board.is_default_piece(first_piece_of_diagonals):
                break

            diagonal_winner = all(piece.type == first_piece_of_diagonals.type for piece in diagonal)

            if diagonal_winner:
                self.winner = self.current_player

    def verify_if_tie(self):
        if self.game_board.is_full:
            self.tie = True

    def register_play(self):
        new_piece_position = self.current_player.current_piece.position
        if not self.game_board.is_default_piece_on_position(new_piece_position):
            return False

        self.game_board.add_piece_to_board(self.current_player.current_piece)
        return True

    def get_gamestatus(self):
        print("Send GameStatus")

        is_over = self.game_over
        end_type = self.end_type
        current_payer = self.current_player.name
        is_valid_move = self.current_player.valid_move
        board = self.game_board.serialize_board
        player_type = self.current_player.pieceType.value
        current_move_row = None
        current_move_col = None
        if self.current_player.current_piece:
            current_move_row = self.current_player.current_piece.position.row
            current_move_col = self.current_player.current_piece.position.col

        return json.dumps({
            'type': 'gamestatus',
            'is_over': is_over,
            'end_type': end_type,
            'current_payer': current_payer,
            'is_valid_move': is_valid_move,
            'board': board,
            'player_type': player_type,
            'current_move_row': current_move_row,
            'current_move_col': current_move_col
        })
