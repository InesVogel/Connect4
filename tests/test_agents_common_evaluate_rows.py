from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, \
    evaluate_rows, is_player_blocking_opponent, is_player_winning


def test_evaluate_rows_True_Player1_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if col == 0 and row > 0:
                game[row - 1][num_cols - 1] = PLAYER2
                apply_player_action(game, 0, PLAYER2)
            elif col < 3:
                apply_player_action(game, col, PLAYER2)
            else:
                game[row][col - 1] = PLAYER2
                apply_player_action(game, col, PLAYER1)

            if col > 2:
                assert evaluate_rows(game, PLAYER1, is_player_blocking_opponent) == True
                assert evaluate_rows(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_rows_True_Player2_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if col == 0 and row > 0:
                game[row - 1][num_cols - 1] = PLAYER1
                apply_player_action(game, 0, PLAYER1)
            elif col < 3:
                apply_player_action(game, col, PLAYER1)
            else:
                game[row][col - 1] = PLAYER1
                apply_player_action(game, col, PLAYER2)

            if col > 2:
                assert evaluate_rows(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_rows(game, PLAYER2, is_player_blocking_opponent) == True


def test_evaluate_rows_False_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            apply_player_action(game, col, PLAYER1)

            if col > 2:
                assert evaluate_rows(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_rows(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_rows_True_Player1_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if col == 0 and row > 0:
                game[row - 1][num_cols - 1] = PLAYER2
                game[row - 1][num_cols - 2] = PLAYER2
                game[row - 1][num_cols - 3] = PLAYER2
                apply_player_action(game, 0, PLAYER1)
            elif col < 4:
                apply_player_action(game, col, PLAYER1)
            else:
                game[row][col - 4] = PLAYER2
                apply_player_action(game, col, PLAYER1)

            if col > 2:
                assert evaluate_rows(game, PLAYER1, is_player_winning) == True
                assert evaluate_rows(game, PLAYER2, is_player_winning) == False


def test_evaluate_rows_True_Player2_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if col == 0 and row > 0:
                game[row - 1][num_cols - 1] = PLAYER1
                game[row - 1][num_cols - 2] = PLAYER1
                game[row - 1][num_cols - 3] = PLAYER1
                apply_player_action(game, 0, PLAYER2)
            elif col < 4:
                apply_player_action(game, col, PLAYER2)
            else:
                game[row][col - 4] = PLAYER1
                apply_player_action(game, col, PLAYER2)

            if col > 2:
                assert evaluate_rows(game, PLAYER1, is_player_winning) == False
                assert evaluate_rows(game, PLAYER2, is_player_winning) == True


def test_evaluate_rows_False_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if col % 2 == 0:
                apply_player_action(game, col, PLAYER2)
            else:
                apply_player_action(game, col, PLAYER1)

            if col > 2:
                assert evaluate_rows(game, PLAYER1, is_player_winning) == False
                assert evaluate_rows(game, PLAYER2, is_player_winning) == False
