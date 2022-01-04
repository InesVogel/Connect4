from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, \
    evaluate_windows_in_diagonal, is_player_blocking_opponent


def test_evaluate_windows_in_diagonal_True_PLAYER1_cols0123():
    cols = {3, 4, 5, 6}

    for col in cols:
        range_begin = col - 3
        range_end = col

        for last_action in range(range_begin, range_end + 1):
            for offset in {0, 1, 2}:
                game = initialize_game_state()

                for idx, k in enumerate(range(range_begin, range_end + 1)):
                    last_row = idx + offset

                    for i in range(0, last_row + 1):
                        if i == last_row and k == last_action:
                            apply_player_action(game, k, PLAYER1)
                        else:
                            apply_player_action(game, k, PLAYER2)

                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER1, is_player_blocking_opponent) == True
                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_diagonal_True_PLAYER2_cols0123():
    cols = {3, 4, 5, 6}

    for col in cols:
        range_begin = col - 3
        range_end = col

        for last_action in range(range_begin, range_end + 1):
            for offset in {0, 1, 2}:
                game = initialize_game_state()

                for idx, k in enumerate(range(range_begin, range_end + 1)):
                    last_row = idx + offset

                    for i in range(0, last_row + 1):
                        if i == last_row and k == last_action:
                            apply_player_action(game, k, PLAYER2)
                        else:
                            apply_player_action(game, k, PLAYER1)

                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER2, is_player_blocking_opponent) == True
                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER1, is_player_blocking_opponent) == False


def test_evaluate_windows_in_diagonal_False_cols456():
    cols = {0, 1, 2}

    for col in cols:
        range_begin = col - 3
        range_end = col

        for last_action in range(range_begin, range_end + 1):
            for offset in {0, 1, 2}:
                game = initialize_game_state()

                for idx, k in enumerate(range(range_begin, range_end + 1)):
                    last_row = idx + offset

                    for i in range(0, last_row + 1):
                        if i == last_row and k == last_action:
                            apply_player_action(game, k, PLAYER2)
                        else:
                            apply_player_action(game, k, PLAYER1)

                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER2, is_player_blocking_opponent) == False
                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER1, is_player_blocking_opponent) == False


def test_evaluate_windows_in_diagonal_False_lastActionOutOfBounds():
    cols = {-1, 7}

    for col in cols:
        range_begin = col - 3
        range_end = col

        for last_action in range(range_begin, range_end + 1):
            for offset in {0, 1, 2}:
                game = initialize_game_state()

                for idx, k in enumerate(range(range_begin, range_end + 1)):
                    last_row = idx + offset

                    for i in range(0, last_row + 1):
                        if i == last_row and k == last_action:
                            apply_player_action(game, k, PLAYER2)
                        else:
                            apply_player_action(game, k, PLAYER1)

                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER2, is_player_blocking_opponent) == False
                assert evaluate_windows_in_diagonal(game, col, last_row, PLAYER1, is_player_blocking_opponent) == False
