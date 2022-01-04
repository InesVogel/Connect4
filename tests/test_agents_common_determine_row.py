from agents.common import PLAYER1, initialize_game_state, apply_player_action, determine_row


def test_determine_row_expect0():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)

    for i in range(0, 6):
        assert determine_row(game, i) == 0


def test_determine_row_expect1():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)

    for i in range(0, 6):
        assert determine_row(game, i) == 1


def test_determine_row_expect2():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)

    for i in range(0, 6):
        assert determine_row(game, i) == 2


def test_determine_row_expect3():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)

    for i in range(0, 6):
        assert determine_row(game, i) == 3


def test_determine_row_expect4():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)

    for i in range(0, 6):
        assert determine_row(game, i) == 4


def test_determine_row_expect5():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)

    for i in range(0, 6):
        assert determine_row(game, i) == 5


def test_determine_row_lastActionOutOfBounds():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)
        apply_player_action(game, i, PLAYER1)

    assert determine_row(game, -1) == -1
    assert determine_row(game, game.shape[1]) == -1
