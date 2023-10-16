from board import Board
from player import Player
from random import randint


class GameLogic:
    current_player = None
    winner = False
    tie = False

    def __init__(self, player1: Player, player2: Player, game_board: Board):
        self.player1 = player1
        self.player2 = player2
        self.game_board = game_board
        self.start()

    def start(self):
        self.draw_player()
        stop = False

        while not stop:
            self.next_player()
            self.current_player.play()

            while not self.register_play():
                if not self.current_player.is_computer:
                    print("Essa casa já está ocupada. Escolha outra...\n")
                self.current_player.play()

            print(f"{self.current_player.name} jogou...\n\n")

            self.verify_if_winner_or_tie()

            if self.winner:
                print(f"The winner is: {self.winner.name}")
                stop = True
            if self.tie:
                print("It is a tie!")
                stop = True

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
