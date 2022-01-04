from agents.agent_minimax import evaluate_windows_in_antidiagonal, is_player_blocking_opponent
from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action


def test_evaluate_windows_in_antidiagonal_True_cols3456_PLAYER1():
    cols = {3, 4, 5, 6}
    cols = {6}

    for col in cols:
        range_begin = 0
        if col == 6:
            range_begin = 1

        for k in range(range_begin, col + 1):
            last_move = k
            last_row = col - k

            game = initialize_game_state()

            for i in range(0, col + 1):
                for j in range(0, col - i + 1):
                    if i == last_move and j == last_row:
                        apply_player_action(game, i, PLAYER1)
                    else:
                        apply_player_action(game, i, PLAYER2)

            assert evaluate_windows_in_antidiagonal(game, last_move, last_row, PLAYER1,
                                                    is_player_blocking_opponent) == True
            assert evaluate_windows_in_antidiagonal(game, last_move, last_row, PLAYER2,
                                                    is_player_blocking_opponent) == False


def test_evaluate_windows_in_antidiagonal_True_cols3456_PLAYER2():
    cols = {3, 4, 5, 6}

    for col in cols:
        range_begin = 0
        if col == 6:
            range_begin = 1

        for k in range(range_begin, col + 1):
            last_move = k
            last_row = col - k

            game = initialize_game_state()

            for i in range(0, col + 1):
                for j in range(0, col - i + 1):
                    if i == last_move and j == last_row:
                        apply_player_action(game, i, PLAYER2)
                    else:
                        apply_player_action(game, i, PLAYER1)

            assert evaluate_windows_in_antidiagonal(game, last_move, last_row, PLAYER2,
                                                    is_player_blocking_opponent) == True
            assert evaluate_windows_in_antidiagonal(game, last_move, last_row, PLAYER1,
                                                    is_player_blocking_opponent) == False


def test_evaluate_windows_in_antidiagonal_False_col012():
    cols = {0, 1, 2}

    for col in cols:
        range_begin = 0
        if col == 6:
            range_begin = 1

        for k in range(range_begin, col + 1):
            last_move = k
            last_row = col - k

            game = initialize_game_state()

            for i in range(0, col + 1):
                for j in range(0, col - i + 1):
                    if i == last_move and j == last_row:
                        apply_player_action(game, i, PLAYER1)
                    else:
                        apply_player_action(game, i, PLAYER2)

            assert evaluate_windows_in_antidiagonal(game, last_move, last_row, PLAYER1,
                                                    is_player_blocking_opponent) == False
            assert evaluate_windows_in_antidiagonal(game, last_move, last_row, PLAYER2,
                                                    is_player_blocking_opponent) == False


def test_evaluate_windows_in_antidiagonal_False_lastActionOutOfBounds():
    cols = {-1, 7}

    for col in cols:
        range_begin = 0
        if col == 6:
            range_begin = 1

        for k in range(range_begin, col + 1):
            last_move = k
            last_row = col - k

            game = initialize_game_state()

            for i in range(0, col + 1):
                for j in range(0, col - i + 1):
                    if i == last_move and j == last_row:
                        apply_player_action(game, i, PLAYER1)
                    else:
                        apply_player_action(game, i, PLAYER2)

            assert evaluate_windows_in_antidiagonal(game, col, last_row, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_windows_in_antidiagonal(game, col, last_row, PLAYER2, is_player_blocking_opponent) == False
