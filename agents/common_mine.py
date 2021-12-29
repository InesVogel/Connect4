# put standard functions and other common dependencies
import numpy as np


class Board:
    def __init__(self, x, y):
        self._num_of_columns = y
        self._num_of_rows = x
        self._num_of_fields = self._num_of_columns * self._num_of_rows
        self._board = np.empty((self._num_of_rows, self._num_of_columns), dtype=object)
        self._next_stone = [x - 1 for i in range(y)]
        self._current_player = 0

    def print_board(self):
        # for i in range(len(self._board)):
        #     for j in range(len(self._board[0])):
        #         print(self._board[i][j], end=' ')
        #     print("\n")
        print(self._board)

    def valid_move(self, player, col):
        print(range(1, self._num_of_columns))
        if player == self._current_player and col in range(1, self._num_of_columns + 1) and self._next_stone[
            col - 1] >= 0:
            return True
        else:
            return False

    def place_stone(self, player, col):
        print("Stein soll in Spalte {}".format(col))
        if self.valid_move(player, col):
            self._board[self._next_stone[col - 1]][col - 1] = player
            self._next_stone[col - 1] -= 1
            self.set_current_player()
            self.print_board()
            print(self._next_stone)
        else:
            print("Move is not valid.")
            self.print_board()

    # def (self):

    def get_current_player(self):
        return self._current_player

    def set_current_player(self):
        if self._current_player == 0:
            self._current_player = 1
        else:
            self._current_player = 0


def init_game(x, y):
    game = Board(x, y)
    return game
