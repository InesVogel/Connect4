import math
from typing import Optional, Tuple

import numpy as np

from agents.common import PlayerAction, BoardPiece, SavedState, check_end_state, GameState, PLAYER1, \
    apply_player_action, PLAYER2
from .common import valid_actions, score_heuristic, DEPTH

ALPHA = -math.inf
BETA = math.inf


def generate_move_alpha_beta(
        board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState] = None
) -> Tuple[PlayerAction, Optional[SavedState]]:
    """
    ....
    """
    score, action, saved_state = alpha_beta_pruning(board, player, DEPTH, -1, ALPHA, BETA, saved_state)
    return action, saved_state


"""
....
"""


def alpha_beta_pruning(board: np.ndarray, player: BoardPiece, depth: int, current, alpha: int, beta: int,
                       saved_state: Optional[SavedState] = None) -> Tuple[float, int, Optional[SavedState]]:
    # TODO: comment docstrings

    # Is Game a draw?
    if check_end_state(board, player) == GameState.IS_DRAW:
        tmp = -math.inf if player == PLAYER1 else math.inf
        return tmp, -1, saved_state

    # Is Game a win? --> blocks win of opponent
    if check_end_state(board, player) == GameState.IS_WIN:
        tmp = math.inf if player == PLAYER1 else -math.inf
        return tmp, -1, saved_state

    # Is depth exhausted?
    if depth == 0:
        player1_score = score_heuristic(board, PLAYER1)
        player2_score = score_heuristic(board, PLAYER2)
        return player1_score + player2_score, -1, saved_state

    # Initilize best_score and best_action
    best_score = -math.inf if player == PLAYER1 else math.inf
    best_action = -1

    # Determine all possible valid actions
    actions = valid_actions(board)

    # Play each possible valid action
    for action in actions:
        copy_board = apply_player_action(board, action, player, True)
        next_player = PLAYER2 if player == PLAYER1 else PLAYER1
        tmp_score = alpha_beta_pruning(copy_board, next_player, depth - 1, alpha, beta, action, saved_state)[0]
        if player == PLAYER1 and tmp_score > best_score:
            best_score = tmp_score
            best_action = action
        elif player == PLAYER2 and tmp_score < best_score:
            best_score = tmp_score
            best_action = action

    # Just for debugging purposes
    if depth == DEPTH - 1:
        print("Col: {} --> Score = {}".format(current, best_score))

    return best_score, best_action, saved_state
