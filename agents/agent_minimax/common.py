import numpy as np

from agents.common import PlayerAction, BoardPiece, NO_PLAYER, PLAYER1, PLAYER2

DEPTH = 4
WindowSize = 4
scoring_dict = {4: 10000,
                3: 1000,
                2: 100,
                }
heuristic_column_index = {
    2: 0,
    3: 0,
    4: 1,
    5: 2,
}


def valid_action(board: np.ndarray, action: int) -> bool:
    """" Return True if last row in column 'action' is empty. """
    return board[-1][action] == NO_PLAYER


def is_player_blocking_opponent(window: np.ndarray, window_size: int, player: BoardPiece) -> bool:
    """ Return True if 'player' blocks win of 'opponent' in 'window'.

    Keyword arguments:
    window -- the representation of connected fields on the board (horizontal, vertical or diagonal)
    window_size -- the number of elements in 'window'
    player -- the player who placed the last BoardPiece on the board
    """
    opponent = PLAYER1 if player == PLAYER2 else PLAYER2

    if np.count_nonzero(window == opponent) == window_size - 1 and np.count_nonzero(window == player) == 1:
        return True
    else:
        return False


def is_win_blocked(board: np.ndarray, player: BoardPiece, last_action: PlayerAction) -> bool:
    """ Return True if 'player' blocks win of 'opponent' on 'board'.

    [more elaborate explanation]

    Keyword arguments:
    board -- the current state of the game
    player -- the player who placed the last BoardPiece on the board
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    """

    # Step 1: fenster auswählen - von last action aus
    # print("Spalte {}: {}".format(last_action, board[:,last_action]))
    row = 5

    for idx, val in enumerate(board[:, last_action]):
        if val == 0:
            # print("Zelle ({})({}) = {}".format(idx-1, last_action, board[idx][last_action]))
            row = idx - 1 if idx != 0 else 0
            break

    # print("Zelle: ({})({}) = {}".format(row, last_action, board[row][last_action]))

    # check Spalte
    if row >= 3:
        window_column = board[row - 3:row + 1, last_action]
        # print("Window Spalte: {}".format(window_column))
        if is_player_blocking_opponent(window_column, WindowSize, player):
            return True

    # check Zeile
    for idx, val in enumerate(board[row]):
        if last_action in range(idx, idx + 4):
            window_row = board[row, idx:idx + 4]
            # print("Window Row = {}".format(window_row))
            if is_player_blocking_opponent(window_row, WindowSize, player):
                return True

    # check diagonale
    if row >= 3 and last_action >= 3:
        window_diagonal = np.array(
            [board[row][last_action], board[row - 1][last_action - 1], board[row - 2][last_action - 2],
             board[row - 3][last_action - 3]])
        # print("Window Diagonal = {}".format(window_diagonal))
        if is_player_blocking_opponent(window_diagonal, WindowSize, player):
            return True

    # check gegendiagonale
    if row >= 3 and last_action <= 3:
        window_gegendiagonal = np.array(
            [board[row][last_action], board[row - 1][last_action + 1], board[row - 2][last_action + 2],
             board[row - 3][last_action + 3]])
        # print("Window Gegendiagonale = {}".format(window_gegendiagonal))
        if is_player_blocking_opponent(window_gegendiagonal, WindowSize, player):
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
    elif tmp_score == best_score and tmp_num_moves < best_num_moves:
        return True
    else:
        return False


def determine_score(window: np.ndarray, window_size: int, player: BoardPiece, next_player: BoardPiece) -> float:
    """ Assign points to 'window' based on 'player'.

    Score is determined based on the following logic:
    - case 1: all fields in window are occupied with pieces of 'player'
    - case 2: all fields except for one are occupied with pieces 'player', remaining field is unoccupied
    - case 3: all fields except for two are occupied with pieces 'player', remaining fields are unoccupied
    - case 4: all fields except for one are occupied with pieces 'next_player', remaining field is unoccupied
    The points for the scoring are defined in the scoring_dict, where the key represents the number of occupied fields.

    Keyword arguments:
    window -- the representation of connected fields on the board (horizontal, vertical or diagonal)
    window_size -- the number of elements in 'window'
    player -- the player who placed the last BoardPiece on the board
    next_player -- the player who will place the next BoardPiece on the board
    """

    if np.count_nonzero(window == player) == window_size:
        return scoring_dict.get(window_size) if player == PLAYER1 else scoring_dict.get(window_size) * (-1)

    elif np.count_nonzero(window == player) == window_size - 1 and np.count_nonzero(window == NO_PLAYER) == 1:
        return scoring_dict.get(window_size - 1) if player == PLAYER1 else scoring_dict.get(window_size - 1) * (-1)

    elif np.count_nonzero(window == player) == window_size - 2 and np.count_nonzero(window == NO_PLAYER) == 2:
        return scoring_dict.get(window_size - 2) if player == PLAYER1 else scoring_dict.get(window_size - 2) * (-1)

    # next_player has chance to win, not a desired outcome
    elif np.count_nonzero(window == next_player) == window_size - 1 and np.count_nonzero(window == NO_PLAYER) == 1:
        return -scoring_dict.get(window_size) if player == PLAYER1 else scoring_dict.get(window_size)

    return 0


def new_score_heuristic(board: np.ndarray, current_player: BoardPiece, next_player: BoardPiece) -> float:
    """
    Calculates a score, which evaluates the current state of the board for player.
    Calculation is based on the number of pieces from player in a connected window of size 4.
    """
    score = 0

    # check columns
    for col in range(len(board[0])):
        num_occupied_fields = np.count_nonzero(board[:, col])
        if (num_occupied_fields >= 2 and num_occupied_fields < 6):
            # print("Col {} with {} occupied fields".format(col, num_occupied_fields))
            for i in range(heuristic_column_index.get(num_occupied_fields), len(board[:, col]) - WindowSize + 1):
                window = board[i:i + WindowSize, col]
                score += determine_score(window, WindowSize, current_player, next_player)

    # check rows
    for row in range(len(board[:, 0])):
        num_occupied_fields = np.count_nonzero(board[row])
        if num_occupied_fields not in {0, len(board[row] - 1)}:
            # print("Row {} with {} occupied fields".format(row, num_occupied_fields))
            for i in range(len(board[row]) - WindowSize + 1):
                window = board[row][i:(i + WindowSize)]
                window_before = np.zeros(4)
                if row == 0:
                    score += determine_score(window, WindowSize, current_player, next_player)
                else:
                    window_before = board[row - 1][i:(i + WindowSize)]
                    if np.count_nonzero(window_before) == 4:
                        score += determine_score(window, WindowSize, current_player, next_player)
    # print("Check Rows finished. Current board score = {}".format(score))

    # check diagonal
    for i in range(len(board[:, 0]) - 3):
        for j in range(len(board[0]) - 3):
            window = np.array([board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]])
            if board[i][j + 1] != NO_PLAYER and board[i + 1][j + 2] != NO_PLAYER and board[i + 2][j + 3] != NO_PLAYER:
                score += determine_score(window, WindowSize, current_player, next_player)

    # check antidiagonal
    for i in range(3, len(board[:, 0])):
        for j in range(len(board[0]) - 3):
            window = np.array([board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]])
            if board[i][j + 1] != NO_PLAYER and board[i - 1][j + 2] != NO_PLAYER and board[i - 2][j + 3] != NO_PLAYER:
                score += determine_score(window, WindowSize, current_player, next_player)

    return score
