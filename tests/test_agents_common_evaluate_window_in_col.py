from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, \
    evaluate_window_in_col, is_player_blocking_opponent


def test_evaluate_window_in_col_lastRowSmalerThanThree_allColumns_False():
    game = initialize_game_state()
    last_row = {0, 1, 2}

    for row in last_row:
        for j in range(0, row):
            for i in range(0, 7):
                apply_player_action(game, i, PLAYER1)

        for i in range(0, 7):
            assert evaluate_window_in_col(game, i, row, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_window_in_col(game, i, row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_window_in_col_lastRowGreaterThanThree_allColumns_False():
    game = initialize_game_state()
    last_row = {3, 4, 5}

    for row in last_row:
        for j in range(0, row):
            for i in range(0, 7):
                apply_player_action(game, i, PLAYER1)

        for i in range(0, 7):
            assert evaluate_window_in_col(game, i, row, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_window_in_col(game, i, row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_window_in_col_lastRowGreaterThanThree_allColumns_True():
    game = initialize_game_state()
    last_row = {3, 4, 5}

    for row in last_row:
        for j in range(0, row + 1):
            for i in range(0, 7):
                if j == row:
                    apply_player_action(game, i, PLAYER2)
                else:
                    apply_player_action(game, i, PLAYER1)

        for i in range(0, 7):
            assert evaluate_window_in_col(game, i, row, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_window_in_col(game, i, row, PLAYER2, is_player_blocking_opponent) == True


def test_evaluate_window_in_col_lastRowSmalerThanThree_lastActionOutOfBounds_allColumns_False():
    game = initialize_game_state()
    last_row = {0, 1, 2}

    for row in last_row:
        for j in range(0, row):
            for i in range(0, 7):
                apply_player_action(game, i, PLAYER1)

        for i in (-1, 7):
            assert evaluate_window_in_col(game, i, row, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_window_in_col(game, i, row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_window_in_col_lastRowGreaterThanThree_lastActionOutOfBounds_allColumns_False():
    game = initialize_game_state()
    last_row = {3, 4, 5, 6}

    for row in last_row:
        for j in range(0, row):
            for i in range(0, 7):
                apply_player_action(game, i, PLAYER1)

        for i in (-1, 7):
            assert evaluate_window_in_col(game, i, row, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_window_in_col(game, i, row, PLAYER2, is_player_blocking_opponent) == False
