import numpy as np

from agents.common import NO_PLAYER, PLAYER1, PLAYER2, string_to_board


def test_string_to_board():
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

    assert string_board[0][3] == PLAYER1
    assert string_board[0][4] == PLAYER1
    assert string_board[0][5] == PLAYER1
    assert string_board[0][6] == PLAYER1
    assert string_board[1][2] == PLAYER1
    assert string_board[2][3] == PLAYER1
    assert string_board[2][4] == PLAYER1
    assert string_board[3][2] == PLAYER1
    assert string_board[3][3] == PLAYER1
    assert string_board[0][1] == PLAYER2
    assert string_board[0][2] == PLAYER2
    assert string_board[1][1] == PLAYER2
    assert string_board[1][3] == PLAYER2
    assert string_board[1][4] == PLAYER2
    assert string_board[2][2] == PLAYER2

    # Assert each row for number of zero values
    assert np.count_nonzero(string_board[0] == NO_PLAYER) == 1
    assert np.count_nonzero(string_board[1] == NO_PLAYER) == 3
    assert np.count_nonzero(string_board[2] == NO_PLAYER) == 4
    assert np.count_nonzero(string_board[3] == NO_PLAYER) == 5
    assert np.count_nonzero(string_board[4] == NO_PLAYER) == 7
    assert np.count_nonzero(string_board[5] == NO_PLAYER) == 7
    # Assert each row for number of one values
    assert np.count_nonzero(string_board[0] == PLAYER1) == 4
    assert np.count_nonzero(string_board[1] == PLAYER1) == 1
    assert np.count_nonzero(string_board[2] == PLAYER1) == 2
    assert np.count_nonzero(string_board[3] == PLAYER1) == 2
    assert np.count_nonzero(string_board[4] == PLAYER1) == 0
    assert np.count_nonzero(string_board[5] == PLAYER1) == 0
    # Assert each row for number of two values
    assert np.count_nonzero(string_board[0] == PLAYER2) == 2
    assert np.count_nonzero(string_board[1] == PLAYER2) == 3
    assert np.count_nonzero(string_board[2] == PLAYER2) == 1
    assert np.count_nonzero(string_board[3] == PLAYER2) == 0
    assert np.count_nonzero(string_board[4] == PLAYER2) == 0
    assert np.count_nonzero(string_board[5] == PLAYER2) == 0
