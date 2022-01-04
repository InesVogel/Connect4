import numpy as np

from agents.agent_minimax import determine_score
from agents.common import PLAYER1, PLAYER2, NO_PLAYER


def test_determine_score_2occupied_singlePlayer_PLAYER1():
    window1 = np.array([PLAYER1, NO_PLAYER, PLAYER1, NO_PLAYER])
    window2 = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, PLAYER1])
    window3 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER1])
    window4 = np.array([NO_PLAYER, PLAYER1, PLAYER1, NO_PLAYER])
    window5 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER1])
    window6 = np.array([PLAYER1, PLAYER1, NO_PLAYER, NO_PLAYER])

    windows = [window1, window2, window3, window4, window5, window6]

    for window in windows:
        assert determine_score(window, 4) == 100


def test_determine_score_2occupied_singlePlayer_PLAYER2():
    window1 = np.array([PLAYER2, NO_PLAYER, PLAYER2, NO_PLAYER])
    window2 = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, PLAYER2])
    window3 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER2])
    window4 = np.array([NO_PLAYER, PLAYER2, PLAYER2, NO_PLAYER])
    window5 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER2])
    window6 = np.array([PLAYER2, PLAYER2, NO_PLAYER, NO_PLAYER])

    windows = [window1, window2, window3, window4, window5, window6]

    for window in windows:
        assert determine_score(window, 4) == -100


def test_determine_score_3occupied_singlePlayer_PLAYER1():
    window1 = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER1])
    window2 = np.array([NO_PLAYER, PLAYER1, PLAYER1, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER1, NO_PLAYER, PLAYER1])
    window4 = np.array([PLAYER1, PLAYER1, PLAYER1, NO_PLAYER])

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert determine_score(window, 4) == 1000


def test_determine_score_3occupied_singlePlayer_PLAYER2():
    window1 = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER2])
    window2 = np.array([NO_PLAYER, PLAYER2, PLAYER2, PLAYER2])
    window3 = np.array([PLAYER2, PLAYER2, NO_PLAYER, PLAYER2])
    window4 = np.array([PLAYER2, PLAYER2, PLAYER2, NO_PLAYER])

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert determine_score(window, 4) == -1000


def test_determine_score_4occupied_singlePlayer_PLAYER1():
    window = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1])
    assert determine_score(window, 4) == 10000


def test_determine_score_4occupied_singlePlayer_PLAYER2():
    window = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2])
    assert determine_score(window, 4) == -10000


def test_determine_score_4occupied_multiplePlayer():
    window = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER1])
    assert determine_score(window, 4) == 0


def test_determine_score_3occupied_multiplePlayer():
    window = np.array([PLAYER1, PLAYER1, PLAYER2, NO_PLAYER])
    assert determine_score(window, 4) == 0


def test_determine_score_2occupied_multiplePlayer():
    window = np.array([NO_PLAYER, PLAYER1, PLAYER2, NO_PLAYER])
    assert determine_score(window, 4) == 0


def test_determine_score_1occupied_singlePlayer_PLAYER1():
    window1 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    window2 = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, NO_PLAYER])
    window3 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER])
    window4 = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER1])

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert determine_score(window, 4) == 0


def test_determine_score_1occupied_singlePlayer_PLAYER2():
    window1 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    window2 = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])
    window3 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER])
    window4 = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2])

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert determine_score(window, 4) == 0
