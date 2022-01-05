from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, \
    evaluate_columns, is_player_blocking_opponent, is_player_winning


def test_evaluate_cols_True_Player1_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            if row == 0 and col > 0:
                game[num_rows - 1][col - 1] = PLAYER2
                apply_player_action(game, col, PLAYER2)
            elif row < 3:
                apply_player_action(game, col, PLAYER2)
            else:
                game[row - 1][col] = PLAYER2
                apply_player_action(game, col, PLAYER1)

            if row > 2:
                assert evaluate_columns(game, PLAYER1, is_player_blocking_opponent) == True
                assert evaluate_columns(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_cols_True_Player2_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            if row == 0 and col > 0:
                game[num_rows - 1][col - 1] = PLAYER1
                apply_player_action(game, col, PLAYER1)
            elif row < 3:
                apply_player_action(game, col, PLAYER1)
            else:
                game[row - 1][col] = PLAYER1
                apply_player_action(game, col, PLAYER2)

            if row > 2:
                assert evaluate_columns(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_columns(game, PLAYER2, is_player_blocking_opponent) == True


def test_evaluate_cols_False_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            apply_player_action(game, col, PLAYER2)

            assert evaluate_columns(game, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_columns(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_columns_True_Player1_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            if row == 0 and col > 0:
                game[num_rows - 1][col - 1] = PLAYER2
                game[num_rows - 2][col - 1] = PLAYER2
                game[num_rows - 3][col - 1] = PLAYER2
                apply_player_action(game, col, PLAYER1)
            elif row < 4:
                apply_player_action(game, col, PLAYER1)
            else:
                game[row - 4][col] = PLAYER2
                apply_player_action(game, col, PLAYER1)

            if row > 2:
                assert evaluate_columns(game, PLAYER1, is_player_winning) == True
                assert evaluate_columns(game, PLAYER2, is_player_winning) == False


def test_evaluate_columns_True_Player2_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            if row == 0 and col > 0:
                game[num_rows - 1][col - 1] = PLAYER1
                game[num_rows - 2][col - 1] = PLAYER1
                game[num_rows - 3][col - 1] = PLAYER1
                apply_player_action(game, col, PLAYER2)
            elif row < 4:
                apply_player_action(game, col, PLAYER2)
            else:
                game[row - 4][col] = PLAYER1
                apply_player_action(game, col, PLAYER2)

            if row > 2:
                assert evaluate_columns(game, PLAYER1, is_player_winning) == False
                assert evaluate_columns(game, PLAYER2, is_player_winning) == True


def test_evaluate_cols_False_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            if row % 2 == 0:
                apply_player_action(game, col, PLAYER2)
            else:
                apply_player_action(game, col, PLAYER1)

            if row > 2:
                assert evaluate_columns(game, PLAYER1, is_player_winning) == False
                assert evaluate_columns(game, PLAYER2, is_player_winning) == False
