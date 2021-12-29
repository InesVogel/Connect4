import numpy as np

from agents.common import BoardPiece, NO_PLAYER, PLAYER1, PLAYER2


# # Test Template for Value Errors
# def test_value_error():
#     with pytest.raises(ValueError):
#         function_name()
#
# # Test Template for Assertions
# def test_assert():
#     assert function_name() == sth


def test_initialize_game_state():
    from agents.common import initialize_game_state

    ret = initialize_game_state()

    assert isinstance(ret, np.ndarray)
    assert ret.dtype == BoardPiece
    assert ret.shape == (6, 7)
    assert np.all(ret == NO_PLAYER)


def test_pretty_print_board_empty():
    from agents.common import initialize_game_state, pretty_print_board

    empty_board = initialize_game_state()
    pretty_print_board(empty_board)
    assert pretty_print_board(empty_board).replace("\n", "") == "" \
                                                                "|==============|" \
                                                                "|              |" \
                                                                "|              |" \
                                                                "|              |" \
                                                                "|              |" \
                                                                "|              |" \
                                                                "|              |" \
                                                                "|==============|" \
                                                                "|0 1 2 3 4 5 6 |"


def test_string_to_board():
    from agents.common import string_to_board

    string_to_convert = "" \
                        "|==============|" \
                        "|              |" \
                        "|              |" \
                        "|    X X       |" \
                        "|    O X X     |" \
                        "|  O X O O     |" \
                        "|  O O X X X X |" \
                        "|==============|" \
                        "|0 1 2 3 4 5 6 |"

    string_board = string_to_board(string_to_convert)

    assert string_board[0][3] == 1
    assert string_board[0][4] == 1
    assert string_board[0][5] == 1
    assert string_board[0][6] == 1
    assert string_board[1][2] == 1
    assert string_board[2][3] == 1
    assert string_board[2][4] == 1
    assert string_board[3][2] == 1
    assert string_board[3][3] == 1
    assert string_board[0][1] == 2
    assert string_board[0][2] == 2
    assert string_board[1][1] == 2
    assert string_board[1][3] == 2
    assert string_board[1][4] == 2
    assert string_board[2][2] == 2

    # Assert each row for number of zero values
    assert np.count_nonzero(string_board[0] == 0) == 1
    assert np.count_nonzero(string_board[1] == 0) == 3
    assert np.count_nonzero(string_board[2] == 0) == 4
    assert np.count_nonzero(string_board[3] == 0) == 5
    assert np.count_nonzero(string_board[4] == 0) == 7
    assert np.count_nonzero(string_board[5] == 0) == 7
    # Assert each row for number of one values
    assert np.count_nonzero(string_board[0] == 1) == 4
    assert np.count_nonzero(string_board[1] == 1) == 1
    assert np.count_nonzero(string_board[2] == 1) == 2
    assert np.count_nonzero(string_board[3] == 1) == 2
    assert np.count_nonzero(string_board[4] == 1) == 0
    assert np.count_nonzero(string_board[5] == 1) == 0
    # Assert each row for number of two values
    assert np.count_nonzero(string_board[0] == 2) == 2
    assert np.count_nonzero(string_board[1] == 2) == 3
    assert np.count_nonzero(string_board[2] == 2) == 1
    assert np.count_nonzero(string_board[3] == 2) == 0
    assert np.count_nonzero(string_board[4] == 2) == 0
    assert np.count_nonzero(string_board[5] == 2) == 0


def test_apply_player_action():
    from agents.common import initialize_game_state, apply_player_action

    game = initialize_game_state()
    apply_player_action(game, 0, PLAYER1)
    assert game[0][0] == 1

    apply_player_action(game, 0, PLAYER2)
    assert game[0][0] == 1
    assert game[1][0] == 2

    apply_player_action(game, 0, PLAYER1)
    assert game[0][0] == 1
    assert game[1][0] == 2
    assert game[2][0] == 1

    apply_player_action(game, 0, PLAYER2)
    assert game[0][0] == 1
    assert game[1][0] == 2
    assert game[2][0] == 1
    assert game[3][0] == 2

    apply_player_action(game, 0, PLAYER1)
    assert game[0][0] == 1
    assert game[1][0] == 2
    assert game[2][0] == 1
    assert game[3][0] == 2
    assert game[4][0] == 1

    apply_player_action(game, 0, PLAYER2)
    assert game[0][0] == 1
    assert game[1][0] == 2
    assert game[2][0] == 1
    assert game[3][0] == 2
    assert game[4][0] == 1
    assert game[5][0] == 2


def test_apply_player_action_copy():
    from agents.common import initialize_game_state, apply_player_action

    game = initialize_game_state()

    copy_game = apply_player_action(game, 1, PLAYER1, True)
    assert game[0][1] == 0
    assert copy_game[0][1] == 1
    assert game[0][1] != copy_game[0][1]


def test_valid_action():
    from agents.common import initialize_game_state, valid_action

    game = initialize_game_state()

    for i in range(0, len(game)):
        assert valid_action(game, i) == True


def test_valid_action_fail():
    from agents.common import initialize_game_state, valid_action

    game = initialize_game_state()

    assert valid_action(game, -1) == False
    assert valid_action(game, 7) == False
    assert valid_action(game, 15) == False


def test_valid_player():
    from agents.common import valid_player

    assert valid_player(0) == True
    assert valid_player(1) == True
    assert valid_player(2) == True
    assert valid_player(3) == False
    assert valid_player(-1) == False


def test_connected_four_column1():
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

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
    from agents.common import initialize_game_state, apply_player_action, connected_four

    game = initialize_game_state()
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 5, PLAYER2)
    apply_player_action(game, 6, PLAYER2)

    # print(pretty_print_board(game))

    assert connected_four(game, PLAYER1, 3) == True
    assert connected_four(game, PLAYER2, 3) == False


def test_check_end_state_win1():
    from agents.common import initialize_game_state, apply_player_action, check_end_state, GameState

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


def test_check_end_state_win2():
    from agents.common import initialize_game_state, apply_player_action, check_end_state, GameState

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


def test_check_end_state_draw1():
    from agents.common import initialize_game_state, apply_player_action, check_end_state, GameState

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
