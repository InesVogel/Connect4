from agents.common import BoardPiece, NO_PLAYER, PLAYER1, PLAYER2, initialize_game_state, apply_player_action


def test_apply_player_action_validAction_validPlayer():
    game_Player1 = initialize_game_state()
    game_Player2 = initialize_game_state()
    num_rows = game_Player1.shape[0]
    num_cols = game_Player1.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            apply_player_action(game_Player1, col, PLAYER1, False)
            apply_player_action(game_Player2, col, PLAYER2, False)

            assert game_Player1[row][col] == PLAYER1
            assert game_Player2[row][col] == PLAYER2


def test_apply_player_action_invalidAction_actionOutOfBounds():
    game_Player1 = initialize_game_state()
    game_Player2 = initialize_game_state()
    num_cols = game_Player1.shape[1]

    for col in {-1, num_cols}:
        tmp_game_Player1 = apply_player_action(game_Player1, col, PLAYER1, True)
        tmp_game_Player2 = apply_player_action(game_Player2, col, PLAYER2, True)

        assert (game_Player1 == tmp_game_Player1).all()
        assert game_Player1.shape == tmp_game_Player1.shape
        assert (game_Player2 == tmp_game_Player2).all()
        assert game_Player2.shape == tmp_game_Player2.shape


def test_apply_player_action_invalidAction_columnFull():
    game_Player1 = initialize_game_state()
    game_Player2 = initialize_game_state()
    num_rows = game_Player1.shape[0]
    num_cols = game_Player1.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows + 1):
            apply_player_action(game_Player1, col, PLAYER1, False)
            apply_player_action(game_Player2, col, PLAYER2, False)

        assert game_Player1[num_rows - 1][col] == PLAYER1
        assert game_Player2[num_rows - 1][col] == PLAYER2


def test_apply_player_action_invalidPlayer():
    game_Player1 = initialize_game_state()
    num_rows = game_Player1.shape[0]
    num_cols = game_Player1.shape[1]

    for col in range(0, num_cols):
        for row in range(0, num_rows):
            apply_player_action(game_Player1, BoardPiece(3), NO_PLAYER, False)

            assert game_Player1[row][col] == NO_PLAYER


def test_apply_player_action_copyBoardTrue():
    game = initialize_game_state()

    copy_game = apply_player_action(game, 1, PLAYER1, True)
    assert game[0][1] == 0
    assert copy_game[0][1] == 1
    assert game[0][1] != copy_game[0][1]
