import numpy as np

from agents.common import PLAYER1, PLAYER2, NO_PLAYER, is_player_winning


def test_is_player_winning_True():
    window1 = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1])
    window2 = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2])

    assert is_player_winning(window1, PLAYER1) == True
    assert is_player_winning(window1, PLAYER2) == False
    assert is_player_winning(window2, PLAYER1) == False
    assert is_player_winning(window2, PLAYER2) == True


def test_is_player_winning_False():
    window1 = np.array([PLAYER2, PLAYER2, PLAYER2, NO_PLAYER])
    window2 = np.array([PLAYER2, PLAYER2, NO_PLAYER, PLAYER2])
    window3 = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER2])
    window4 = np.array([NO_PLAYER, PLAYER2, PLAYER2, PLAYER2])
    window5 = np.array([PLAYER1, PLAYER1, PLAYER1, NO_PLAYER])
    window6 = np.array([PLAYER1, PLAYER1, NO_PLAYER, PLAYER1])
    window7 = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER1])
    window8 = np.array([NO_PLAYER, PLAYER1, PLAYER1, PLAYER1])

    windows = [window1, window2, window3, window4, window5, window6, window7, window8]

    for window in windows:
        assert is_player_winning(window, PLAYER1) == False
        assert is_player_winning(window, PLAYER2) == False
