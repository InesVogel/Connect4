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

dict_next_player = {PLAYER1: PLAYER2,
                    PLAYER2: PLAYER1}

PlayerAction = np.int8  # The column to be played

DEPTH = 4
WindowSize = 4
scoring_dict = {4: 10000,
                3: 1000,
                2: 100,
                1: 0,
                0: 0
                }
heuristic_column_index = {
    2: 0,
    3: 0,
    4: 1,
    5: 2,
}

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


# TODO: what should happen if action is not valid? (e.g. action out of bounds or column is full)
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


def connected_four_optimized(board: np.ndarray, player: BoardPiece, last_action: PlayerAction) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.
    If desired, the last action taken (i.e. last column played) can be provided
    for potential speed optimisation.
    """

    row = determine_row(board, last_action)

    if evaluate_window_in_col(board, last_action, row, player, is_player_winning):
        return True

    if evaluate_windows_in_row(board, last_action, row, player, is_player_winning):
        return True

    if evaluate_windows_in_diagonal(board, last_action, row, player, is_player_winning):
        return True

    if evaluate_windows_in_antidiagonal(board, last_action, row, player, is_player_winning):
        return True

    return False


def is_player_winning(window: np.ndarray, player: BoardPiece) -> bool:
    """ Return True if 'player' achieves a win with 'window'.

    A win is achieved if all fields of window are occupied with BoardPieces from 'player'

    Keyword arguments:
    window -- the representation of connected fields on the board (horizontal, vertical or diagonal)
    player -- the player who placed the last BoardPiece on the board
    """

    return True if count_occupied_fields(window, player) == window.__len__() else False


def evaluate_rows(board: np.ndarray, player, eval_function) -> bool:
    """ Return True if 'eval_function' for one window in rows evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    for row in range(len(board[:, 0])):
        for i in range(len(board[row]) - 3):
            window = np.array([board[row][i],
                               board[row][i + 1],
                               board[row][i + 2],
                               board[row][i + 3]])

            if eval_function(window, player):
                return True

    return False


def evaluate_columns(board: np.ndarray, player, eval_function) -> bool:
    """ Return True if 'eval_function' for one window in columns evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    for col in range(len(board[0])):
        for i in range(len(board[:, col]) - 3):
            window = np.array([board[i][col],
                               board[i + 1][col],
                               board[i + 2][col],
                               board[i + 3][col]])

            if eval_function(window, player):
                return True

    return False


def evaluate_diagonals(board: np.ndarray, player, eval_function) -> bool:
    """ Return True if 'eval_function' for one diagonal window evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    for i in range(len(board[:, 0]) - 3):
        for j in range(len(board[0]) - 3):
            window = np.array([board[i][j],
                               board[i + 1][j + 1],
                               board[i + 2][j + 2],
                               board[i + 3][j + 3]])

            if eval_function(window, player):
                return True

    return False


def evaluate_antidiagonals(board: np.ndarray, player, eval_function) -> bool:
    """ Return True if 'eval_function' for one window in a antidiagonal evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    for i in range(3, len(board[:, 0])):
        for j in range(len(board[0]) - 3):
            window = np.array([board[i][j],
                               board[i - 1][j + 1],
                               board[i - 2][j + 2],
                               board[i - 3][j + 3]])

            if eval_function(window, player):
                return True

    return False


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

    if evaluate_columns(board, player, is_player_winning):
        return True

    if evaluate_rows(board, player, is_player_winning):
        return True

    if evaluate_antidiagonals(board, player, is_player_winning):
        return True

    if evaluate_diagonals(board, player, is_player_winning):
        return True

    return False


def is_game_draw(board) -> bool:
    """ Returns True if 'board' is a draw. """

    if np.count_nonzero(board[-1]) == len(board[0]):
        return True
    else:
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
    elif is_game_draw(board):
        return GameState.IS_DRAW
    else:
        return GameState.STILL_PLAYING


def next_player(player: BoardPiece) -> BoardPiece:
    """" Return player, who will put the next BoardPiece on the board. """

    return NO_PLAYER if dict_next_player.get(player) is None else dict_next_player.get(player)


def is_valid_action(board: np.ndarray, action: int) -> bool:
    """" Return True if last row in column 'action' is empty. """

    tmp = range(0, board.__len__() + 1)
    if action in tmp:
        return board[-1][action] == NO_PLAYER
    else:
        return False


def is_player_blocking_opponent(window: np.ndarray, player: BoardPiece) -> bool:
    """ Return True if 'player' blocks win of next player in 'window'.

    Next players win is blocked if one field in 'window' is occupied by 'player' and
    all other fields are occupied by next player.

    Keyword arguments:
    window -- the representation of connected fields on the board (horizontal, vertical or diagonal)
    player -- the player who placed the last BoardPiece on the board
    """

    window_size = window.__len__()

    if count_occupied_fields(window, next_player(player)) == window_size - 1 and \
            count_occupied_fields(window, player) == 1:
        return True
    else:
        return False


def determine_row(board: np.ndarray, last_action: PlayerAction) -> int:
    """ Determine row which contains last BoardPiece placed on board.

    Keyword arguments:
    board -- the current state of the game
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    """
    if last_action not in range(0, board.shape[1]):
        return -1

    # print("Spalte {}: {}".format(last_action, board[:,last_action]))
    row = board.__len__() - 1

    for idx, val in enumerate(board[:, last_action]):
        if val == 0:
            # print("Zelle ({})({}) = {}".format(idx-1, last_action, board[idx][last_action]))
            row = idx - 1 if idx != 0 else 0
            break

    return row


def determine_start_row_col_for_diagonal(last_action: PlayerAction, last_row: int):
    """ Determine start field (= row and column) of diagonal.

    Keyword arguments:
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    last_row -- the last row on 'board' where a BoardPiece was placed
    """

    if last_row <= last_action:
        return 0, last_action - last_row
    else:
        return last_row - last_action, 0


def determine_num_windows_for_diagonal(board: np.ndarray, start_col: PlayerAction, start_row: int) -> int:
    """ Determine number of windows with WindowSize for given diagonal.

    Keyword arguments:
    board -- the current state of the game
    start_col -- the column where the diagonal starts
    start_row -- the row where the diagonal starts
    """
    num_rows = board.shape[0]
    num_cols = board.shape[1]

    if start_col <= 1 and num_rows - WindowSize >= start_row:
        return num_rows - start_row - WindowSize + 1
    elif 1 < start_col < WindowSize and start_row == 0:
        return num_cols - start_col - WindowSize + 1
    else:
        return 0


def determine_start_row_col_for_antidiagonal(board: np.ndarray, last_action: PlayerAction, last_row: int):
    """ Determine start field (= row and column) of antidiagonal.

    Keyword arguments:
    board -- the current state of the game
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    last_row -- the last row on 'board' where a BoardPiece was placed
    """

    num_rows = board.shape[0]

    if last_action + last_row < num_rows:
        return last_action + last_row, 0
    else:
        return num_rows - 1, last_action + last_row - num_rows + 1


def determine_num_windows_for_antidiagonal(board: np.ndarray, start_col: PlayerAction, start_row: int) -> int:
    """ Determine number of windows with WindowSize for given diagonal.

    Keyword arguments:
    board -- the current state of the game
    start_col -- the column where the antidiagonal starts
    start_row -- the row where the antidiagonal starts
    """

    num_cols = board.shape[1]

    if start_col == 0 and start_row > 2:
        return (start_row + 1) % WindowSize + 1
    elif 0 < start_col < WindowSize:
        return (num_cols - start_col) % WindowSize + 1
    else:
        return 0


def evaluate_windows_in_row(board: np.ndarray, last_action: PlayerAction, last_row: int, player, eval_function) -> bool:
    """ Return True if 'eval_function' for one window in 'last_row' evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    last_row -- the row containing last BoardPiece that was placed on 'board'
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    for i in range(0, 4):
        if last_action in range(i, i + WindowSize):
            window = board[last_row, i:i + WindowSize]
            # print("Window Row = {}".format(window))
            if eval_function(window, player):
                return True

    return False


def evaluate_window_in_col(board: np.ndarray, last_action: PlayerAction, last_row: int, player, eval_function) -> bool:
    """ Return True if 'eval_function' for last window in 'last_action' evaluates to True.

    The last window in 'last_action' represents the four connecting fields from last_row to the bottom of the 'board'

    Keyword arguments:
    board -- the current state of the game
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    last_row -- the row containing last BoardPiece that was placed on 'board'
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    if last_row >= 3 and last_action < 7:
        window = board[last_row - 3:last_row + 1, last_action]
        # print("Window Spalte: {}".format(window))
        if eval_function(window, player):
            return True

    return False


def evaluate_windows_in_diagonal(
        board: np.ndarray, last_action: PlayerAction, last_row: int, player, eval_function
) -> bool:
    """ Return True if 'eval_function' for one diagonal window evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    last_row -- the row containing last BoardPiece that was placed on 'board'
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    if 0 <= last_action < 7:
        row, col = determine_start_row_col_for_diagonal(last_action, last_row)

        range_end = determine_num_windows_for_diagonal(board, col, row)
        for i in range(0, range_end):
            window = np.array([board[row][col],
                               board[row + 1][col + 1],
                               board[row + 2][col + 2],
                               board[row + 3][col + 3]])

            if eval_function(window, player):
                return True

            row = row + 1
            col = col + 1

    return False


def evaluate_windows_in_antidiagonal(
        board: np.ndarray, last_action: PlayerAction, last_row: int, player, eval_function
) -> bool:
    """ Return True if 'eval_function' for one antidiagonal window evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    last_row -- the row containing last BoardPiece that was placed on 'board'
    player -- the player who placed the last BoardPiece on the board
    eval_function -- the function that should be evaluated for chosen window
    """

    if 0 <= last_action < 7:
        row, col = determine_start_row_col_for_antidiagonal(board, last_action, last_row)

        range_end = determine_num_windows_for_antidiagonal(board, col, row)
        for i in range(0, range_end):
            window = np.array([board[row][col],
                               board[row - 1][col + 1],
                               board[row - 2][col + 2],
                               board[row - 3][col + 3]])

            if eval_function(window, player):
                return True

            row = row - 1
            col = col + 1

    return False


def is_win_blocked(board: np.ndarray, player: BoardPiece, last_action: PlayerAction) -> bool:
    """ Return True if 'player' blocks win of next player on 'board'.

    The win of next player is blocked if is_player_blocking_opponent() evaluates to True.

    Keyword arguments:
    board -- the current state of the game
    player -- the player who placed the last BoardPiece on the board
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    """

    row = determine_row(board, last_action)

    if evaluate_window_in_col(board, last_action, row, player, is_player_blocking_opponent):
        return True

    if evaluate_windows_in_row(board, last_action, row, player, is_player_blocking_opponent):
        return True

    if evaluate_windows_in_diagonal(board, last_action, row, player, is_player_blocking_opponent):
        return True

    if evaluate_windows_in_antidiagonal(board, last_action, row, player, is_player_blocking_opponent):
        return True

    return False


def is_result_better(
        best_score: float, best_num_moves: int, tmp_score: float, tmp_num_moves: int, player: BoardPiece
) -> bool:
    """ Return True if 'tmp_score' and/or 'tmp_num_moves' is better for 'player' than current best.

    Keyword arguments:
    best_score -- the current best score
    best_num_moves -- the current best number of recursive calls at which 'best_score' was achieved
    tmp_score -- the potential better score
    tmp_num_moves -- the potential number of recursive calls at which 'tmp_score' was achieved
    player -- the player who placed the last BoardPiece on the board
    """
    if player == PLAYER1 and tmp_score > best_score:
        return True
    elif player == PLAYER2 and tmp_score < best_score:
        return True
    # TODO: figure out if this is  actually needed (?)
    elif tmp_score == best_score and tmp_num_moves < best_num_moves:
        return True
    else:
        return False


def count_occupied_fields(window, player):
    """" Count number of occupied fields by 'player' in 'window'. """

    count = np.count_nonzero(window == player)

    return 0 if count is None else count


def determine_score(window: np.ndarray, window_size: int) -> float:
    """ Assign points to 'window' based on number of pieces in window.

    Score is determined based on the following logic:
    - case 1: all fields in window are occupied with pieces of a single player
    - case 2: all fields except for one are occupied with pieces of a single player, remaining field is unoccupied
    - case 3: all fields except for two are occupied with pieces of a single player, remaining fields are unoccupied
    The points for the scoring are defined in the scoring_dict, where the key represents the number of occupied fields.

    Keyword arguments:
    window -- the representation of connected fields on the board (horizontal, vertical or diagonal)
    window_size -- the number of elements in 'window'
    """

    num_fields_player1 = count_occupied_fields(window, PLAYER1)
    num_fields_player2 = count_occupied_fields(window, PLAYER2)
    num_fields_free = count_occupied_fields(window, NO_PLAYER)

    if (num_fields_player2 + num_fields_player1 + num_fields_free) == window_size:
        if num_fields_player2 == 0:
            return scoring_dict.get(num_fields_player1)
        elif num_fields_player1 == 0:
            return scoring_dict.get(num_fields_player2) * (-1)

    return 0


def heuristic(board: np.ndarray) -> float:
    """ Assign score to current state of 'board'.

    Score is calculated based on the number of pieces from a player in a connected window of size 4.

    Keyword arguments:
    board -- the representation of connected fields on the board (horizontal, vertical or diagonal)
    player -- the player who placed the last BoardPiece on the 'board'
    """
    score = 0

    # check columns
    for col in range(len(board[0])):
        num_occupied_fields = np.count_nonzero(board[:, col])
        if (num_occupied_fields >= 2 and num_occupied_fields < 6):
            # print("Col {} with {} occupied fields".format(col, num_occupied_fields))
            for i in range(heuristic_column_index.get(num_occupied_fields), len(board[:, col]) - WindowSize + 1):
                window = board[i:i + WindowSize, col]
                score += determine_score(window, WindowSize)

    # check rows
    for row in range(len(board[:, 0])):
        num_occupied_fields = np.count_nonzero(board[row])
        if num_occupied_fields not in {0, len(board[row] - 1)}:
            # print("Row {} with {} occupied fields".format(row, num_occupied_fields))
            for i in range(len(board[row]) - WindowSize + 1):
                window = board[row][i:(i + WindowSize)]
                window_before = np.zeros(4)
                if row == 0:
                    score += determine_score(window, WindowSize)
                else:
                    window_before = board[row - 1][i:(i + WindowSize)]
                    if np.count_nonzero(window_before) == 4:
                        score += determine_score(window, WindowSize)
    # print("Check Rows finished. Current board score = {}".format(score))

    # check diagonal
    for i in range(len(board[:, 0]) - 3):
        for j in range(len(board[0]) - 3):
            window = np.array([board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]])
            if board[i][j + 1] != NO_PLAYER and board[i + 1][j + 2] != NO_PLAYER and board[i + 2][j + 3] != NO_PLAYER:
                score += determine_score(window, WindowSize)

    # check antidiagonal
    for i in range(3, len(board[:, 0])):
        for j in range(len(board[0]) - 3):
            window = np.array([board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]])
            if board[i][j + 1] != NO_PLAYER and board[i - 1][j + 2] != NO_PLAYER and board[i - 2][j + 3] != NO_PLAYER:
                score += determine_score(window, WindowSize)

    return score
