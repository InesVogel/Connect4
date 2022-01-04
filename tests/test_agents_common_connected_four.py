from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, \
    connected_four


# # Test Template for Value Errors
# def test_value_error():
#     with pytest.raises(ValueError):
#         function_name()
#
# # Test Template for Assertions
# def test_assert():
#     assert function_name() == sth


def test_connected_four_column1():
    game = initialize_game_state()
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    assert connected_four(game, PLAYER1) == True
    assert connected_four(game, PLAYER2) == False


def test_connected_four_column2():
    game = initialize_game_state()
    col = 4
    apply_player_action(game, col, PLAYER2)
    apply_player_action(game, col, PLAYER1)
    apply_player_action(game, col, PLAYER2)
    apply_player_action(game, col, PLAYER1)
    apply_player_action(game, col, PLAYER2)
    apply_player_action(game, col, PLAYER2)

    assert connected_four(game, PLAYER1) == False
    assert connected_four(game, PLAYER2) == False


def test_connected_four_column3():
    game = initialize_game_state()
    col = 0
    apply_player_action(game, col, PLAYER1)
    apply_player_action(game, col, PLAYER1)
    apply_player_action(game, col, PLAYER2)
    apply_player_action(game, col, PLAYER2)
    apply_player_action(game, col, PLAYER2)
    apply_player_action(game, col, PLAYER2)

    assert connected_four(game, PLAYER1) == False
    assert connected_four(game, PLAYER2) == True


def test_connected_four_row1():
    game = initialize_game_state()
    row = 1
    apply_player_action(game, row, PLAYER1)
    apply_player_action(game, row + 1, PLAYER1)
    apply_player_action(game, row + 2, PLAYER2)
    apply_player_action(game, row + 3, PLAYER2)
    apply_player_action(game, row + 4, PLAYER2)
    apply_player_action(game, row + 5, PLAYER2)

    assert connected_four(game, PLAYER1) == False
    assert connected_four(game, PLAYER2) == True


def test_connected_four_row2():
    game = initialize_game_state()
    row = 1
    apply_player_action(game, row, PLAYER1)
    apply_player_action(game, row + 1, PLAYER2)
    apply_player_action(game, row + 2, PLAYER2)
    apply_player_action(game, row + 3, PLAYER1)
    apply_player_action(game, row + 4, PLAYER2)
    apply_player_action(game, row + 5, PLAYER1)
    row = 0
    apply_player_action(game, row, PLAYER2)
    apply_player_action(game, row + 1, PLAYER1)
    apply_player_action(game, row + 2, PLAYER1)
    apply_player_action(game, row + 3, PLAYER1)
    apply_player_action(game, row + 4, PLAYER1)
    apply_player_action(game, row + 5, PLAYER2)

    assert connected_four(game, PLAYER1) == True
    assert connected_four(game, PLAYER2) == False


def test_connected_four_antidiagonal1():
    game = initialize_game_state()
    apply_player_action(game, 5, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)

    assert connected_four(game, PLAYER1) == True
    assert connected_four(game, PLAYER2) == False


def test_connected_four_antidiagonal2():
    game = initialize_game_state()
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 1, PLAYER1)

    assert connected_four(game, PLAYER1) == True
    assert connected_four(game, PLAYER2) == False


def test_connected_four_antidiagonal3():
    game = initialize_game_state()
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 1, PLAYER2)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 6, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 3, PLAYER2)

    assert connected_four(game, PLAYER1) == False
    assert connected_four(game, PLAYER2) == True


def test_connected_four_diagonal1():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)

    assert connected_four(game, PLAYER1) == True
    assert connected_four(game, PLAYER2) == False


def test_connected_four_diagonal2():
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

    assert connected_four(game, PLAYER1) == True
    assert connected_four(game, PLAYER2) == False


def test_connected_four_diagonal3():
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

    assert connected_four(game, PLAYER1) == False
    assert connected_four(game, PLAYER2) == True


def test_connected_four_last_action_column1():
    game = initialize_game_state()
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    assert connected_four(game, PLAYER1, 3) == True
    assert connected_four(game, PLAYER2, 3) == False
