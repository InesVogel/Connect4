from agents.common import PLAYER1, PLAYER2, initialize_game_state, evaluate_antidiagonals, is_player_blocking_opponent, \
    is_player_winning


def test_evaluate_antidiagonals_uppertriangle_True_Player1_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_col = 0
    for row in range(0, num_rows):
        last_row = 0
        for col in range(0, num_cols):
            if last_row < 0:
                break
            if col == 0 and row > 0:
                game[0][last_col] = PLAYER2
                game[row][col] = PLAYER2
            elif col < 3:
                game[row - col][col] = PLAYER2
            elif col < 4:
                game[row - col][col] = PLAYER1
            else:
                game[row - col + 1][col - 1] = PLAYER2
                game[row - col][col] = PLAYER1
            last_row = row - col - 1
            last_col = col

            if col > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == True
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False

            if col < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_antidiagonals_uppertriangle_True_Player2_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_col = 0
    for row in range(0, num_rows):
        last_row = 0
        for col in range(0, num_cols):
            if last_row < 0:
                break
            if col == 0 and row > 0:
                game[0][last_col] = PLAYER1
                game[row][col] = PLAYER1
            elif col < 3:
                game[row - col][col] = PLAYER1
            elif col < 4:
                game[row - col][col] = PLAYER2
            else:
                game[row - col + 1][col - 1] = PLAYER1
                game[row - col][col] = PLAYER2
            last_row = row - col - 1
            last_col = col

            if col > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == True

            if col < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_antidiagonals_uppertriangle_False_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        last_row = 0
        for col in range(0, num_cols):
            if last_row < 0:
                break

            game[row - col][col] = PLAYER2

            last_row = row - col - 1

            assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_antidiagonals_lowertriangle_True_Player1_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_row = num_rows - 1
    for col in range(1, num_cols):
        last_col = 1
        for row in range(num_rows - 1, -1, -1):
            if last_col == num_cols - 1:
                break
            if row == num_rows - 1 and col > 1:
                game[last_row][num_cols - 1] = PLAYER2
                game[row][col] = PLAYER2
            elif row > 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            elif row == 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER1
            else:
                game[row + 1][num_cols - row - 1 + col - 2] = PLAYER2
                game[row][num_cols - row - 1 + col - 1] = PLAYER1
            last_row = row
            last_col = num_cols - row - 1 + col - 1

            if row < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == True
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False

            if row > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_antidiagonals_lowertriangle_True_Player2_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_row = num_rows - 1
    for col in range(1, num_cols):
        last_col = 1
        for row in range(num_rows - 1, -1, -1):
            if last_col == num_cols - 1:
                break
            if row == num_rows - 1 and col > 1:
                game[last_row][num_cols - 1] = PLAYER1
                game[row][col] = PLAYER1
            elif row > 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER1
            elif row == 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            else:
                game[row + 1][num_cols - row - 1 + col - 2] = PLAYER1
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            last_row = row
            last_col = num_cols - row - 1 + col - 1

            if row < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == True

            if row > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_antidiagonals_lowertriangle_False_is_player_blocking_opponent():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(1, num_cols):
        last_col = 1
        for row in range(num_rows - 1, -1, -1):
            if last_col == num_cols - 1:
                break

            game[row][num_cols - row - 1 + col - 1] = PLAYER2

            last_col = num_cols - row - 1 + col - 1

            assert evaluate_antidiagonals(game, PLAYER1, is_player_blocking_opponent) == False
            assert evaluate_antidiagonals(game, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_antidiagonals_uppertriangle_True_Player1_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_col = 0
    for row in range(0, num_rows):
        last_row = 0
        for col in range(0, num_cols):
            if last_row < 0:
                break
            if col == 0 and row > 0:
                game[0][last_col] = PLAYER2
                game[row][col] = PLAYER1
            elif col < 4:
                game[row - col][col] = PLAYER1
            else:
                game[row - col + 4][col - 4] = PLAYER2
                game[row - col][col] = PLAYER1
            last_row = row - col - 1
            last_col = col

            if col > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == True
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False

            if col < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False


def test_evaluate_antidiagonals_uppertriangle_True_Player2_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_col = 0
    for row in range(0, num_rows):
        last_row = 0
        for col in range(0, num_cols):
            if last_row < 0:
                break
            if col == 0 and row > 0:
                game[0][last_col] = PLAYER1
                game[row][col] = PLAYER2
            elif col < 4:
                game[row - col][col] = PLAYER2
            else:
                game[row - col + 4][col - 4] = PLAYER1
                game[row - col][col] = PLAYER2
            last_row = row - col - 1
            last_col = col

            if col > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == True

            if col < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False


def test_evaluate_antidiagonals_uppertriangle_False_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for row in range(0, num_rows):
        last_row = 0
        for col in range(0, num_cols):
            if last_row < 0:
                break

            if col % 2 == 0:
                game[row - col][col] = PLAYER2
            else:
                game[row - col][col] = PLAYER1

            last_row = row - col - 1

            assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
            assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False


def test_evaluate_antidiagonals_lowertriangle_True_Player1_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_row = num_rows - 1
    for col in range(1, num_cols):
        last_col = 1
        for row in range(num_rows - 1, -1, -1):
            if last_col == num_cols - 1:
                break
            if row == num_rows - 1 and col > 1:
                game[last_row][num_cols - 1] = PLAYER2
                game[row][col] = PLAYER1
            elif row > 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER1
            elif row == 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER1
            else:
                game[row + 4][num_cols - row - 1 + col - 5] = PLAYER2
                game[row][num_cols - row - 1 + col - 1] = PLAYER1
            last_row = row
            last_col = num_cols - row - 1 + col - 1

            if row < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == True
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False

            if row > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False


def test_evaluate_antidiagonals_lowertriangle_True_Player2_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    last_row = num_rows - 1
    for col in range(1, num_cols):
        last_col = 1
        for row in range(num_rows - 1, -1, -1):
            if last_col == num_cols - 1:
                break
            if row == num_rows - 1 and col > 1:
                game[last_row][num_cols - 1] = PLAYER1
                game[row][col] = PLAYER2
            elif row > 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            elif row == 2:
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            else:
                game[row + 4][num_cols - row - 1 + col - 5] = PLAYER1
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            last_row = row
            last_col = num_cols - row - 1 + col - 1

            if row < 3:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == True

            if row > 2:
                assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
                assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False


def test_evaluate_antidiagonals_lowertriangle_False_is_player_winning():
    game = initialize_game_state()
    num_rows = game.shape[0]
    num_cols = game.shape[1]

    for col in range(1, num_cols):
        last_col = 1
        for row in range(num_rows - 1, -1, -1):
            if last_col == num_cols - 1:
                break

            if row % 2 == 0:
                game[row][num_cols - row - 1 + col - 1] = PLAYER2
            else:
                game[row][num_cols - row - 1 + col - 1] = PLAYER1

            last_col = num_cols - row - 1 + col - 1

            assert evaluate_antidiagonals(game, PLAYER1, is_player_winning) == False
            assert evaluate_antidiagonals(game, PLAYER2, is_player_winning) == False
