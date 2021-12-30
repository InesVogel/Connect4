import numpy as np

from agents.agent_minimax import determine_score
from agents.common import PLAYER1, PLAYER2, NO_PLAYER


def test_determine_score_2occupied_singlePlayer_PLAYER1():
    window = np.array([PLAYER1, NO_PLAYER, PLAYER1, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 100
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 100
    assert score_Player2 == 0

    window = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 100
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, PLAYER1, PLAYER1, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 100
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 100
    assert score_Player2 == 0

    window = np.array([PLAYER1, PLAYER1, NO_PLAYER, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 100
    assert score_Player2 == 0


def test_determine_score_2occupied_singlePlayer_PLAYER2():
    window = np.array([PLAYER2, NO_PLAYER, PLAYER2, NO_PLAYER])
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    assert score_Player2 == -100
    assert score_Player1 == 0

    window = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, PLAYER2])
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    assert score_Player2 == -100
    assert score_Player1 == 0

    window = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER2])
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    assert score_Player2 == -100
    assert score_Player1 == 0

    window = np.array([NO_PLAYER, PLAYER2, PLAYER2, NO_PLAYER])
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    assert score_Player2 == -100
    assert score_Player1 == 0

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER2])
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    assert score_Player2 == -100
    assert score_Player1 == 0

    window = np.array([PLAYER2, PLAYER2, NO_PLAYER, NO_PLAYER])
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    assert score_Player2 == -100
    assert score_Player1 == 0


def test_determine_score_3occupied_singlePlayer_PLAYER1():
    window = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 1000
    assert score_Player2 == 10000

    window = np.array([NO_PLAYER, PLAYER1, PLAYER1, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 1000
    assert score_Player2 == 10000

    window = np.array([PLAYER1, PLAYER1, NO_PLAYER, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 1000
    assert score_Player2 == 10000

    window = np.array([PLAYER1, PLAYER1, PLAYER1, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 1000
    assert score_Player2 == 10000


def test_determine_score_3occupied_singlePlayer_PLAYER2():
    window = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER2])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == -10000
    assert score_Player2 == -1000

    window = np.array([NO_PLAYER, PLAYER2, PLAYER2, PLAYER2])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == -10000
    assert score_Player2 == -1000

    window = np.array([PLAYER2, PLAYER2, NO_PLAYER, PLAYER2])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == -10000
    assert score_Player2 == -1000

    window = np.array([PLAYER2, PLAYER2, PLAYER2, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == -10000
    assert score_Player2 == -1000


def test_determine_score_4occupied_singlePlayer_PLAYER1():
    window = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)

    assert score_Player1 == 10000
    assert score_Player2 == 0


def test_determine_score_4occupied_singlePlayer_PLAYER2():
    window = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)

    assert score_Player1 == 0
    assert score_Player2 == -10000


def test_determine_score_4occupied_multiplePlayer():
    window = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0


def test_determine_score_3occupied_multiplePlayer():
    window = np.array([PLAYER1, PLAYER1, PLAYER2, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0


def test_determine_score_2occupied_multiplePlayer():
    window = np.array([NO_PLAYER, PLAYER1, PLAYER2, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0


def test_determine_score_1occupied_singlePlayer_PLAYER1():
    window = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER1])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0


def test_determine_score_1occupied_singlePlayer_PLAYER2():
    window = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0

    window = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2])
    score_Player1 = determine_score(window, 4, PLAYER1, PLAYER2)
    score_Player2 = determine_score(window, 4, PLAYER2, PLAYER1)
    assert score_Player1 == 0
    assert score_Player2 == 0
