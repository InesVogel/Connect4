import random
from typing import Optional, Tuple

import numpy as np

from agents.common import PlayerAction, BoardPiece, SavedState, NO_PLAYER


def generate_move_random(
        board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState] = None
) -> Tuple[PlayerAction, Optional[SavedState]]:
    # Choose a valid, non-full column randomly and return it as `action`

    action = None
    while True:
        action = random.randint(0, len(board[0]) - 1)
        if board[5][action] == NO_PLAYER:
            break

    return action, saved_state
