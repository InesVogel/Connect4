import math
from typing import Optional, Tuple

import numpy as np

from agents.common import PlayerAction, BoardPiece, SavedState, check_end_state, GameState, PLAYER1, \
    apply_player_action, PLAYER2
from .common import valid_action, DEPTH, is_win_blocked, \
    is_result_better, new_score_heuristic


# possible_moves = set()
# scores = np.zeros(6)

def generate_move_minimax(
        board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState] = None
) -> Tuple[PlayerAction, Optional[SavedState]]:
    """
    ....
    """

    score, action, saved_state, num_moves = minimax(board, player, DEPTH, -1, saved_state)

    return action, saved_state

    # if action != -1:
    #     return action, saved_state
    # else:
    #     tmp = random.choice(list(possible_moves))
    #     return tmp , saved_state


"""
....
"""


def minimax(board: np.ndarray, player: BoardPiece, depth: int, last_action,
            saved_state: Optional[SavedState] = None) -> Tuple[float, int, Optional[SavedState]]:
    # TODO: comment docstrings
    tmp_num_moves = DEPTH - depth

    # Is Game a draw?
    if check_end_state(board, player) == GameState.IS_DRAW:
        tmp = -math.inf if player == PLAYER1 else math.inf
        return tmp, last_action, saved_state, tmp_num_moves

    # Is Game a win? --> higher prio than blocking opponent
    previous_player = PLAYER2 if player == PLAYER1 else PLAYER1
    if check_end_state(board, previous_player) == GameState.IS_WIN:
        tmp = math.inf if previous_player == PLAYER1 else -math.inf
        return tmp, last_action, saved_state, tmp_num_moves

    # Is Opponent win blocked? --> second highest prio otherwise game is over after opponents next move
    if is_win_blocked(board, previous_player, last_action):
        # print("Win blocked at depth = {} with {} moves by Player = {}".format(depth, tmp_num_moves, previous_player))
        tmp = 10000 if previous_player == PLAYER1 else -10000
        return tmp, last_action, saved_state, tmp_num_moves

    # Is depth exhausted?
    if depth == 0:
        tmp = new_score_heuristic(board, previous_player, player)
        return tmp, last_action, saved_state, tmp_num_moves

    # Initilize best_score, best_action and best_num_moves
    best_score = -math.inf if player == PLAYER1 else math.inf
    best_action = -1
    best_num_moves = math.inf

    # Determine priority of columns
    ## TODO: calculate order of columns based on current board
    actions = [3, 4, 2, 5, 1, 6, 0]

    # Play each possible valid action
    for action in actions:
        if valid_action(board, action):
            ## TOODO: instead of making a move introduce do and undo move
            copy_board = apply_player_action(board, action, player, True)
            next_player = PLAYER2 if player == PLAYER1 else PLAYER1
            tmp_score, tmp_action, saved_state, tmp_num_moves = minimax(copy_board, next_player, depth - 1, action,
                                                                        saved_state)

            if is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, player):
                best_score = tmp_score
                best_action = action
                best_num_moves = tmp_num_moves

    return best_score, best_action, saved_state, depth
