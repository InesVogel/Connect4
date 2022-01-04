import math
from typing import Optional, Tuple

import numpy as np

from agents.common import PlayerAction, BoardPiece, apply_player_action, check_end_state, SavedState, GameState, \
    PLAYER2, PLAYER1, is_valid_action, is_win_blocked, is_result_better, heuristic, DEPTH


def generate_move_minimax_alpha_beta_pruning(
        board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState] = None
) -> Tuple[PlayerAction, Optional[SavedState]]:
    """ Choose a valid, non-full column using minimax algorithm with alpha beta pruning and return it as `action`.

    Keyword arguments:
    board -- the current state of the game
    player -- the player for whom the next PlayerAction is determined
    saved_state -- optional (not being used currently)
    """
    action = PlayerAction(-1)
    alpha = -math.inf
    beta = math.inf
    score, num_moves, action = alpha_beta_pruning(board, player, DEPTH, action, alpha, beta, saved_state)

    return action, saved_state


def alpha_beta_pruning(
        board: np.ndarray, player: BoardPiece, depth: int, last_action: PlayerAction, alpha: float, beta: float,
        saved_state: Optional[SavedState] = None
) -> Tuple[float, int, PlayerAction]:
    # TODO: comment docstrings
    """Return best score, best number of moves and best action for 'player'.

    Keyword arguments:
    board -- the current state of the game
    player -- the player for whom the best action is determined
    depth -- the number of recursive steps left of the minimax algorithm
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    alpha -- the current best score for the maximizing player
    beta -- the current best score for the minimizing player
    saved_state -- optional (not being used currently)
    """

    """ Terminate minimax. """
    tmp_score, tmp_num_moves = terminate_minimax(board, player, depth, last_action)
    if tmp_score != -1:
        return tmp_score, tmp_num_moves, last_action

    """ Initilize best_score, best_action and best_num_moves. """
    best_score = -math.inf if player == PLAYER1 else math.inf
    best_action = -1
    best_num_moves = math.inf

    """ Determine order(=priority) of columns. """
    # TODO: calculate order of columns based on current board
    actions = [PlayerAction(3), PlayerAction(4), PlayerAction(2), PlayerAction(5),
               PlayerAction(1), PlayerAction(6), PlayerAction(0)]

    """ Play each possible valid action. """
    for action in actions:
        if is_valid_action(board, action):
            # TODO: instead of copying board introduce do and undo move/action
            copy_board = apply_player_action(board, action, player, True)
            next_player = PLAYER2 if player == PLAYER1 else PLAYER1
            tmp_score, tmp_num_moves, tmp_action = alpha_beta_pruning(copy_board, next_player, depth - 1, action,
                                                                      alpha, beta, saved_state)

            """ Determine best_score. """
            if is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, player):
                best_score = tmp_score
                best_action = action
                best_num_moves = tmp_num_moves

                if player == PLAYER1:
                    alpha = max(alpha, best_score)
                elif player == PLAYER2:
                    beta = min(beta, best_score)

            # # Debugging purposes
            # if depth == DEPTH:
            #     print("Col {} - score: {} - current_best_score: {}".format(action, tmp_score, best_score))

            """ Determine alpha or beta cutoff. """
            if is_alpha_beta_cutoff(player, alpha, beta):
                break

    return best_score, best_num_moves, best_action


def terminate_minimax(
        board: np.ndarray, player: BoardPiece, depth: int, last_action: PlayerAction
) -> Tuple[float, int]:
    """Determine termination option of minimax algorithm.

    Keyword arguments:
    board -- the current state of the game
    player -- the player for whom the termination option is determined
    depth -- the number of recursive steps left of the minimax algorithm
    last_action -- the last column chosen on 'board' where a BoardPiece was placed
    """

    tmp_num_moves = DEPTH - depth
    previous_player = PLAYER2 if player == PLAYER1 else PLAYER1

    if check_end_state(board, player) == GameState.IS_DRAW:  # Most undesired outcome therefore lowest score
        tmp = -math.inf if player == PLAYER1 else math.inf
        return tmp, tmp_num_moves

    if check_end_state(board, previous_player) == GameState.IS_WIN:  # Most desired outcome therefore highest score
        tmp = math.inf if previous_player == PLAYER1 else -math.inf
        return tmp, tmp_num_moves

    if is_win_blocked(board, previous_player, last_action):  # Second most desired outcome hence second highest score
        tmp = 10000 if previous_player == PLAYER1 else -10000
        return tmp, tmp_num_moves

    if depth == 0:  # Recursion depth exhausted
        tmp = heuristic(board)
        return tmp, tmp_num_moves

    return -1, tmp_num_moves


def is_alpha_beta_cutoff(player: BoardPiece, alpha: float, beta: float) -> bool:
    """Return True if alpha-cutoff or beta-cutoff occurs.

    Keyword arguments:
    player -- the player for whom the alpha- or beta-cutoff is determined
    alpha -- the current best score for the maximizing player
    beta -- the current best score for the minimizing player
    """

    if player == PLAYER1 and alpha >= beta:
        return True
    elif player == PLAYER2 and beta <= alpha:
        return True
    else:
        return False
