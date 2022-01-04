import numpy as np

from agents.agent_minimax import is_player_blocking_opponent
from agents.common import PLAYER1, PLAYER2, NO_PLAYER


def test_is_player_blocking_opponent_2blocks1():
    window1 = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER2])
    window2 = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER1])
    window4 = np.array([PLAYER2, PLAYER1, PLAYER1, PLAYER1])

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER1) == False
        assert is_player_blocking_opponent(window, PLAYER2) == True


def test_is_player_blocking_opponent_1blocks2():
    window1 = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER1])
    window2 = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER2])
    window3 = np.array([PLAYER2, PLAYER1, PLAYER2, PLAYER2])
    window4 = np.array([PLAYER1, PLAYER2, PLAYER2, PLAYER2])

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == True


def test_is_player_blocking_opponent_false_singleFieldOccupied_singlePlayer():
    window1 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    window2 = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])
    window3 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER])
    window4 = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2])
    window5 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    window6 = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, NO_PLAYER])
    window7 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER])
    window8 = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER1])

    windows = [window1, window2, window3, window4, window5, window6, window7, window8]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_twoFieldsOccupied_singlePlayer():
    window1 = np.array([PLAYER2, PLAYER2, NO_PLAYER, NO_PLAYER])
    window2 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER2])
    window3 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER2])
    window4 = np.array([PLAYER1, PLAYER1, NO_PLAYER, NO_PLAYER])
    window5 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER1])
    window6 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER1])

    windows = [window1, window2, window3, window4, window5, window6]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_twoFieldsOccupied_multiplePlayer():
    window1 = np.array([PLAYER2, PLAYER1, NO_PLAYER, NO_PLAYER])
    window2 = np.array([PLAYER1, PLAYER2, NO_PLAYER, NO_PLAYER])
    window3 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER1])
    window4 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER2])
    window5 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER2])
    window6 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER1])

    windows = [window1, window2, window3, window4, window5, window6]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_threeFieldsOccupied_singlePlayer():
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
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_threeFieldsOccupied_multiplePlayer():
    window1 = np.array([PLAYER1, PLAYER2, PLAYER2, NO_PLAYER])
    window2 = np.array([PLAYER2, PLAYER1, NO_PLAYER, PLAYER2])
    window3 = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER1])
    window4 = np.array([NO_PLAYER, PLAYER1, PLAYER2, PLAYER2])
    window5 = np.array([PLAYER1, PLAYER1, PLAYER2, NO_PLAYER])
    window6 = np.array([PLAYER2, PLAYER1, NO_PLAYER, PLAYER1])
    window7 = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER2])
    window8 = np.array([NO_PLAYER, PLAYER1, PLAYER2, PLAYER1])

    windows = [window1, window2, window3, window4, window5, window6, window7, window8]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_fourFieldsOccupied_singlePlayer():
    window1 = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2])
    window2 = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1])

    windows = [window1, window2]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_fourFieldsOccupied_multiplePlayer():
    window1 = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER2])
    window2 = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER2, PLAYER2, PLAYER1])
    window4 = np.array([PLAYER2, PLAYER1, PLAYER1, PLAYER2])
    window5 = np.array([PLAYER2, PLAYER1, PLAYER2, PLAYER1])
    window6 = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER2])

    windows = [window1, window2, window3, window4, window5, window6]

    for window in windows:
        assert is_player_blocking_opponent(window, PLAYER2) == False
        assert is_player_blocking_opponent(window, PLAYER1) == False
