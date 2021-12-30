from enum import Enum
from typing import Callable, Tuple
from typing import Optional

import numpy as np

BoardPiece = np.int8  # The data type (dtype) of the board
NO_PLAYER = BoardPiece(0)  # board[i, j] == NO_PLAYER where the position is empty
PLAYER1 = BoardPiece(1)  # board[i, j] == PLAYER1 where player 1 (player to move first) has a piece
PLAYER2 = BoardPiece(2)  # board[i, j] == PLAYER2 where player 2 (player to move second) has a piece

BoardPiecePrint = str  # dtype for string representation of BoardPiece
NO_PLAYER_PRINT = BoardPiecePrint(' ')
PLAYER1_PRINT = BoardPiecePrint('X')
PLAYER2_PRINT = BoardPiecePrint('O')

board_dict = {NO_PLAYER: NO_PLAYER_PRINT,
              PLAYER1: PLAYER1_PRINT,
              PLAYER2: PLAYER2_PRINT}

reverse_board_dict = {NO_PLAYER_PRINT: NO_PLAYER,
                      PLAYER1_PRINT: PLAYER1,
                      PLAYER2_PRINT: PLAYER2}

PlayerAction = np.int8  # The column to be played


class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0


class SavedState:
    pass


GenMove = Callable[
    [np.ndarray, BoardPiece, Optional[SavedState]],  # Arguments for the generate_move function
    Tuple[PlayerAction, Optional[SavedState]]  # Return type of the generate_move function
]


def initialize_game_state() -> np.ndarray:
    """
    Returns an ndarray, shape (6, 7) and data type (dtype) BoardPiece, initialized to 0 (NO_PLAYER).
    """
    return np.full((6, 7), NO_PLAYER)


def pretty_print_board(board: np.ndarray) -> str:
    """
    Should return `board` converted to a human readable string representation,
    to be used when playing or printing diagnostics to the console (stdout). The piece in
    board[0, 0] should appear in the lower-left. Here's an example output, note that we use
    PLAYER1_Print to represent PLAYER1 and PLAYER2_Print to represent PLAYER2):
    |==============|
    |              |
    |              |
    |    X X       |
    |    O X X     |
    |  O X O O     |
    |  O O X X     |
    |==============|
    |0 1 2 3 4 5 6 |
    """
    print_board = "|==============|\n"
    for row in range(len(board) - 1, -1, -1):
        print_board += "|"
        for col in range(len(board[0])):
            print_board += board_dict[board[row][col]]
            print_board += " "
        print_board += "|\n"
    print_board += "|==============|\n"
    print_board += "|0 1 2 3 4 5 6 |\n"

    return print_board


def string_to_board(pp_board: str) -> np.ndarray:
    """
    Takes the output of pretty_print_board and turns it back into an ndarray.
    This is quite useful for debugging, when the agent crashed and you have the last
    board state as a string.
    """
    board = initialize_game_state()

    rows = pp_board.split("||")
    col_counter = 0
    row_index = len(board) - 1
    for row in rows:
        # print("Row: {} -> {}".format(row_index, row))
        if row.startswith("|=") or row.startswith("0 1 2 3") or row.startswith("="):
            continue
        else:
            for i, char in enumerate(row):
                if i % 2 == 0:
                    # print("{} -> {}:{}".format(i, col_counter, char))
                    board[row_index][col_counter] = reverse_board_dict.get(char)
                    col_counter += 1
            col_counter = 0
            row_index -= 1

    return board


def valid_action(board: np.ndarray, action: PlayerAction) -> bool:
    """
    Helper Function  for apply_player_action(...): validates proposed action
    by checking if action is within board boundaries
    """
    return True if action in range(0, len(board[0])) else False


def valid_player(player: BoardPiece) -> bool:
    """
    Helper Function for apply_player_action(...): validates proposed player
    by checking player value against board_dict
    """
    return True if player in board_dict else False


def apply_player_action(
        board: np.ndarray, action: PlayerAction, player: BoardPiece, copy: bool = False
) -> np.ndarray:
    """
    Sets board[i, action] = player, where i is the lowest open row. The modified
    board is returned. If copy is True, makes a copy of the board before modifying it.
    """
    copy_board = np.copy(board) if copy else board

    if valid_action(copy_board, action) and valid_player(player):
        for row in range(0, len(copy_board[:, action])):
            # print("Zeile {}/{} - Inhalt: {}".format(row, len(board[:,action])-1, board[row][action]))
            if copy_board[row][action] == NO_PLAYER:
                copy_board[row][action] = player
                break

    return copy_board


def undo_apply_player_action(
        board: np.ndarray, last_action: PlayerAction, player: BoardPiece
):
    """
    Sets board[i, last_action] = 0, where i is the lowest occupied row by player.
    """

    if valid_player(player):
        for row in range(1, len(board[:, last_action])):
            if board[row][last_action] == NO_PLAYER and board[row - 1][last_action] == player:
                board[row - 1][last_action] = NO_PLAYER
                break


def connected_four_optimized(board: np.ndarray, player: BoardPiece, last_action: PlayerAction) -> bool:
    # check column=last_action
    row = len(board)
    # print(range(len(board[:, last_action]) - 3))
    for i in range(len(board[:, last_action])):
        if i < 4 and board[i][last_action] == player and board[i + 1][last_action] == player \
                and board[i + 2][last_action] == player and board[i + 3][last_action] == player:
            # print("Found 4 adjacent pieces for Player {} in column {}".format(player, last_action))
            return True
        if i == NO_PLAYER:
            row = i - 1

    # check row:
    for i in range(len(board[row]) - 3):
        if board[row][i] == player and board[row][i + 1] == player and board[row][i + 2] == player and \
                board[row][i + 3] == player:
            # print("Found 4 adjacent pieces for Player {} in row {}".format(player, row))
            return True

    return False


# TODO: implement last_action
# TODO: optimize implementation
def connected_four(
        board: np.ndarray, player: BoardPiece, last_action: Optional[PlayerAction] = None,
) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.
    If desired, the last action taken (i.e. last column played) can be provided
    for potential speed optimisation.
    """

    if last_action != None:
        # print("execute connected_four_optimized() with last action = {}".format(last_action))
        return connected_four_optimized(board, player, last_action)

    # check columns
    for col in range(len(board[0])):
        # print("Column {}".format(col))
        for i in range(len(board[:, col]) - 3):
            if board[i][col] == player and board[i + 1][col] == player \
                    and board[i + 2][col] == player and board[i + 3][col] == player:
                # print("Found 4 adjacent pieces for Player {} in column {}".format(player, col))
                return True

    # check rows:
    for row in range(len(board[:, 0])):
        # print("Row {}".format(row))
        for i in range(len(board[row]) - 3):
            if board[row][i] == player and board[row][i + 1] == player and board[row][i + 2] == player and \
                    board[row][i + 3] == player:
                # print("Found 4 adjacent pieces for Player {} in row {}".format(player, row))
                return True

    # check antidiagonal
    for i in range(3, len(board[:, 0])):
        for j in range(len(board[0]) - 3):
            # print("Check {}{} == {}".format(i,j,board[i][j]))
            if board[i][j] == player and board[i - 1][j + 1] == player and board[i - 2][j + 2] == player and \
                    board[i - 3][j + 3] == player:
                return True

    # check diagonal
    for i in range(len(board[:, 0]) - 3):
        for j in range(len(board[0]) - 3):
            # print("Check {}{} == {}".format(i,j,board[i][j]))
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and \
                    board[i + 3][j + 3] == player:
                return True

    return False


def check_end_state(
        board: np.ndarray, player: BoardPiece, last_action: Optional[PlayerAction] = None,
) -> GameState:
    """
    Returns the current game state for the current `player`, i.e. has their last
    action won (GameState.IS_WIN) or drawn (GameState.IS_DRAW) the game,
    or is play still on-going (GameState.STILL_PLAYING)?
    """
    if connected_four(board, player, last_action):
        return GameState.IS_WIN
    else:
        return GameState.IS_DRAW if np.count_nonzero(board[-1]) == len(board[0]) else GameState.STILL_PLAYING
