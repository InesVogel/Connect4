from agents.common import PLAYER1, PLAYER2, string_to_board, is_win_blocked


def test_is_win_blocked_diagonal():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|        X     |" \
                  "|      O X     |" \
                  "|    O X O     |" \
                  "|  O X X O O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    assert is_win_blocked(board, PLAYER1, 4) == True
    assert is_win_blocked(board, PLAYER2, 4) == False


def test_is_win_blocked_antidiagonal():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|    X   X     |" \
                  "|    X O X     |" \
                  "|    O X O     |" \
                  "|  X O X O O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    assert is_win_blocked(board, PLAYER1, 2) == True
    assert is_win_blocked(board, PLAYER2, 2) == False


def test_is_win_blocked_col():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|    X O X     |" \
                  "|    X X X     |" \
                  "|    O X O     |" \
                  "|  X O X O O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    assert is_win_blocked(board, PLAYER1, 3) == False
    assert is_win_blocked(board, PLAYER2, 3) == True


def test_is_win_blocked_row():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|      X O O O |" \
                  "|  X O X O O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    assert is_win_blocked(board, PLAYER1, 3) == True
    assert is_win_blocked(board, PLAYER2, 3) == False


def test_is_win_blocked_False():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|      X O X O |" \
                  "|  X O X O O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    assert is_win_blocked(board, PLAYER1, 3) == False
    assert is_win_blocked(board, PLAYER2, 3) == False
