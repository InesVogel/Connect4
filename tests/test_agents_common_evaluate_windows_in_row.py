from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, \
    evaluate_windows_in_row, is_player_blocking_opponent


def test_evaluate_windows_in_row0_True_window0123():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)

    for i in range(0, 4):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == True


def test_evaluate_windows_in_row0_False_window0123():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)

    for i in range(0, 4):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row0_True_window1234():
    game = initialize_game_state()

    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER2)

    for i in range(1, 5):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == True
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row0_False_window1234():
    game = initialize_game_state()

    apply_player_action(game, 1, PLAYER1)

    for i in range(1, 5):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row0_True_window2345():
    game = initialize_game_state()

    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)

    for i in range(2, 6):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == True
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row0_False_window2345():
    game = initialize_game_state()

    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)

    for i in range(2, 6):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row0_True_window3456():
    game = initialize_game_state()

    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    for i in range(3, 7):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == True
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row0_False_window3456():
    game = initialize_game_state()

    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    for i in range(3, 7):
        assert evaluate_windows_in_row(game, i, 0, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, 0, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_True_window0123():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)

    for i in range(0, 4):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == True


def test_evaluate_windows_in_row5_False_window0123():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)

    for i in range(0, 4):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_True_window1234():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER2)

    for i in range(1, 5):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == True
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_False_window1234():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 1, PLAYER1)

    for i in range(1, 5):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_True_window2345():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)

    for i in range(2, 6):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == True
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_False_window2345():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)

    for i in range(2, 6):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_True_window3456():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    for i in range(3, 7):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == True
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_False_window3456():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    for i in range(3, 7):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False


def test_evaluate_windows_in_row5_False_window3456_lastActionOutOfBounds():
    game = initialize_game_state()

    last_row = 5

    for j in range(0, last_row):
        for i in range(0, 7):
            apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    for i in (-1, 7):
        assert evaluate_windows_in_row(game, i, last_row, PLAYER1, is_player_blocking_opponent) == False
        assert evaluate_windows_in_row(game, i, last_row, PLAYER2, is_player_blocking_opponent) == False
