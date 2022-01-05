from agents.common import PLAYER1, PLAYER2, GameState, initialize_game_state, apply_player_action, check_end_state


def test_check_end_state_win_Player2():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)
    apply_player_action(game, 6, PLAYER2)
    apply_player_action(game, 6, PLAYER1)
    apply_player_action(game, 6, PLAYER2)

    assert check_end_state(game, PLAYER2) == GameState.IS_WIN
    assert check_end_state(game, PLAYER1) == GameState.STILL_PLAYING


def test_check_end_state_win_Player1():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 4, PLAYER1)

    assert check_end_state(game, PLAYER1) == GameState.IS_WIN
    assert check_end_state(game, PLAYER2) == GameState.STILL_PLAYING


def test_check_end_state_draw():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER1)
    apply_player_action(game, 6, PLAYER2)
    apply_player_action(game, 6, PLAYER1)
    apply_player_action(game, 6, PLAYER1)
    apply_player_action(game, 5, PLAYER1)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)
    apply_player_action(game, 6, PLAYER2)
    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER2)

    assert check_end_state(game, PLAYER2) == GameState.IS_DRAW
    assert check_end_state(game, PLAYER1) == GameState.IS_DRAW
